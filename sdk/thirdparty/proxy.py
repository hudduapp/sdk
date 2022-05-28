import ast
import json

import redis


class Proxy:

    def __init__(self, url: str):
        """

        @param url:
        """
        self.url = url
        self.db = redis.from_url(url)

    def create_or_update_proxy_route(self, target_domain: str, source_domain: str, fallback_domains: list,
                                     ) -> dict:
        """
        ssl will be handled by a *.domain.ending cert
        @param fallback_domains:
        @param target_domain:
        @param source_domain:
        @return:
        """
        config = {
            "sourceDomain": source_domain,
            "fallbackDomains": fallback_domains
        }
        self.db.set(target_domain, json.dumps(config))  # redis only takes bytes or strings
        return config

    def get_route(self, domain: str) -> dict:
        data = self.db.get(domain).decode("utf-8")
        return ast.literal_eval(data)  # not properly tested

    def delete_route(self, domain: str) -> None:
        self.db.delete([domain])
