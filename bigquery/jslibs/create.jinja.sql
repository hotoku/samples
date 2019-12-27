#standardSQL

select * from unnest(
[
{% for obj in list_ %}
   {% if loop.index > 1 %} , {% endif %}
   struct(
     "{{ obj.name }}" as name,
     jslibs.h3.ST_H3_POLYFILLFROMGEOG(
       ST_GEOGFROMTEXT(
         "{{ obj.polygon }}"
       )
     ) as polygon_str
   ) as feature         
{% endfor %}
]
)
