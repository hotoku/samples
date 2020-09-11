from jinja2 import Template

x = Template("""
{%- macro mymacro(x, y, z) -%}
{{x}} - {{y}} - {{z}}
{%- endmacro -%}

{{ mymacro(1, 2, 3) }}

""").render({})

print(x)


y = Template("""
{%- macro m1(x) -%}
x - x
{%- endmacro -%}
{%- macro m2(x) -%}
{{ m1(x) }}
{%- endmacro -%}
{{ m2(1) }}
""").render({})

print(y)
# マクロは2重には展開されない
