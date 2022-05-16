# Overview

## Django Recap

- Django's roots
  - MTV pattern
  - early 2000s web development
  - written for applications used to publish articles
- Django model/view/template
  - model (persistent data)
  - view (logic)
  - template (document parsed and returned to the browser)
- Django needs javascript (inevitable)
  - cons: maintenance issue
    - javacript libraries 
    - javascript libraries update frequently

## What is htmx?

- Javascript library
- extends html, DSL
- pairs well with django templates

- Talks specifically about htmx
- [here](https://youtu.be/cBfz4W_KvEI?list=PLPxWAqiM9MhdKV6kiX2Ofa-mVKATzVVj9)
- [here](https://youtu.be/u2rjnLJ1M98?list=PLPxWAqiM9MhdKV6kiX2Ofa-mVKATzVVj9)

## Why would you use htmx?

### Developer

- Improve long term maintenance
- No javascript maintenance
- DSL is easy to understand

### Application

- "Dynamic" feel for the user
- Optimized responses

## Examples

### Form submission

- emphasis on improvements to Django's POST/Redirect/GET pattern

### Page fragments

- emphasis on response fragments returned

### Form validation

- emphasis on having one true source of validation (backend)
- provide early feedback (for errors) in the front-end

### Dropdowns

- avoid json apis, generate plain html

### Modal Windows

- displaying modal windows

### Django Admin

- ways to use htmx on Django Admin
