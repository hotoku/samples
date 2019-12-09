FROM rocker/shiny-verse



RUN install2.r --error future promises

RUN mkdir -p /srv/shiny-server/app/{1,2}
COPY app_01.r /srv/shiny-server/app/1/app.r
COPY app_02.r /srv/shiny-server/app/2/app.r
RUN sudo chown -R shiny:shiny /srv/shiny-server



EXPOSE 3838

CMD ["/usr/bin/shiny-server.sh"]
