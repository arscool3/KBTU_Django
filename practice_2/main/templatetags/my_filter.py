from django import template

register = template.Library()

@register.filter
def get_year(stud_id: str) -> str:
  return stud_id[:2]

@register.filter
def get_degree(stud_id: str) -> str:
  if stud_id[2:3] == 'B':
    return 'Bachelor'
  elif stud_id[2:3] == 'M':
    return 'Master'