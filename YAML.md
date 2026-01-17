## What does a regular YAML file look like?
```yaml
---
# A sample yaml file
company: Legion
domain:
 - devops
 - devsecops
tutorial:
  - yaml:
      name: "YAML Ain't Markup Language"
      type: awesome
      born: 2001
  - json:
      name: JavaScript Object Notation
      type: great
      born: 2001
  - xml:
      name: Extensible Markup Language
      type: good
      born: 1996
author: krsna
published: true
```
----
## Basic Syntax of a YAML
A YAML format primarily uses three node types:

1. **Maps/Dictionaries** (YAML calls it _mapping_)  
    The content of a _mapping_ node is an unordered set of _key/value_ node _pairs_, with the restriction that each of the keys is unique. YAML places no further restrictions on the nodes.
2. **Arrays/Lists** (YAML calls them _sequences_)  
    The content of a _sequence_ node is an ordered series of zero or more nodes. In particular, a sequence may contain the same node more than once. It could even contain itself.
3. **Literals** (Strings, numbers, boolean, etc.)  
    The content of a _scalar_ node is an opaque datum that can be presented as a series of zero or more _Unicode characters_.
