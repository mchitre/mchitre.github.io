#!/usr/bin/python

import re, bibtexparser

with open('all.bib') as f:
  db = bibtexparser.load(f)

shown = []

def my(bib):
  if 'Excellence in Review' in bib['title']:
    return False
  if 'author' not in bib:
    return False
  if re.search('Chitre', bib['author'], re.IGNORECASE):
    return True
  return False

def invited(bib):
  if 'note' in bib:
    if re.search('invited', bib['note'], re.IGNORECASE):
      return True
    if re.search('plenary', bib['note'], re.IGNORECASE):
      return True
    if re.search('keynote', bib['note'], re.IGNORECASE):
      return True
  return False

def authors(s):
  a3 = []
  a = s.split(" and ")
  for a1 in a:
    a2 = a1.split(", ")
    a2 = a2[0].split(" ")[-1]
    if a2 == 'Chitre':
      a2 = "**Chitre**"
    a3.append(a2)
  s1 = ""
  if len(a3) == 1:
    return a3[0]
  for i in range(len(a3)-1):
    s1 = s1 + a3[i] + ", "
  s1 = s1[:-2] + " and " + a3[-1]
  return s1

def title(s):
  if s.isupper():
    s = s.title()
  if "Editorial " in s:
    s = s.replace("Editorial ", "Editorial: ")
  return re.sub(r"[\\{\\}]", "", s)

def vnp(bib):
  s = ""
  if 'volume' in bib:
    s = s + ', ' + bib['volume']
    if 'number' in bib:
      s = s + '(' + bib['number'] + ')'
  if 'pages' in bib:
    s = s + ', p' + bib['pages']
  return s

def format(bib):
  if bib['ENTRYTYPE'] == 'incollection':
    s = authors(bib['author'])+', "'+title(bib['title'])+'", '+title(bib['booktitle'])+' ('+bib['editor']+', eds.), p' + bib['pages']+', '+bib['publisher']+', '+bib['year']+'.'
  elif bib['ENTRYTYPE'] == 'article':
    s = authors(bib['author'])+', "'+title(bib['title'])+'", '+title(bib['journal'])+vnp(bib)+', '+bib['year']+'.'
  elif bib['ENTRYTYPE'] == 'conference':
    s = authors(bib['author'])+', "'+title(bib['title'])+'", '+title(bib['booktitle'])+', '+bib['year']+'.'
  elif 'thesis' in bib['ENTRYTYPE']:
    s = authors(bib['author'])+', "'+title(bib['title'])+'", '+title(bib['school'])+', '+bib['year']+'.'
  else:
    s = authors(bib['author'])+', "'+title(bib['title'])+'", '+title(bib['howpublished'])+', '+bib['year']+'.'
  s1 = []
  if 'doi' in bib:
    s1.append('[doi](http://dx.doi.org/' + bib['doi']+")")
  if 'http' in bib:
    s1.append('[web](' + bib['http']+")")
  if 'pdf' in bib:
    url = bib['pdf']
    if 'http' not in url:
      url = 'https://arl.nus.edu.sg' + url
    s1.append('[pdf](' + url+")")
  if len(s1) > 0:
    s = s + ' ['+('\\|'.join(s1))+']'
  return s

def show(db, filt):
  toshow = []
  for bib in db.entries:
    if my(bib) and bib['ID'] not in shown and filt(bib):
      toshow.append(bib)
      shown.append(bib['ID'])
  toshow.sort(key=lambda bib: bib['year'], reverse=True)
  i = 1
  for bib in toshow:
    print(str(i)+". "+format(bib))
    i = i + 1

print("""\
---
title: Publications
layout: page
hero_height: is-fullwidth
hero_image: assets/images/head6.jpg
---""")

print("\n### Journal Papers\n")
show(db, lambda bib: bib['ENTRYTYPE'] == 'article')

print("\n### Books & Chapters\n")
show(db, lambda bib: bib['ENTRYTYPE'] == 'incollection')

print("\n### Keynote / Plenary / Invited Talks\n")
show(db, lambda bib: bib['ENTRYTYPE'] == 'conference' and invited(bib))

print("\n### Conference Papers\n")
show(db, lambda bib: bib['ENTRYTYPE'] == 'conference')

print("\n### Thesis\n")
show(db, lambda bib: 'thesis' in bib['ENTRYTYPE'])

print("\n### Others\n")
show(db, lambda bib: True)
