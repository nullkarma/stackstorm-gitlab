#!/usr/bin/env python

from lib.gitlab import GitlabPipelineAPI


class GitlabPipeline(GitlabPipelineAPI):

    def run(self, url, project, ref, token, verify_ssl):
        self.url = url or self.url
        self.verify_ssl = verify_ssl or self.verify_ssl
        self.token = token or self.token

        return True, self.post(self.url, project, params={"ref": ref})
