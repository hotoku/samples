from scrapy.pipelines.images import FilesPipeline
import re


class CovidPdfPipeline(FilesPipeline):
    def file_path(self, request, response=None, info=None):
        original_path = super(CovidPdfPipeline, self).file_path(request, response=None, info=None)
        sha1_and_extension = original_path.split('/')[1]  # delete 'full/' from the path
        filename = re.sub(".+/([^/]+).pdf$", r"\1", request.url)
        return f"{filename}_{sha1_and_extension}"
