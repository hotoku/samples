#standardSQL

select * from unnest(
[
{% for obj in list_ %}
   {% if loop.index > 1 %} , {% endif %}
   struct(
     "{{ obj.name }}" as name,
     "{{ obj.polygon }}" as polygon_str
   ) as feature         
{% endfor %}
]
)
