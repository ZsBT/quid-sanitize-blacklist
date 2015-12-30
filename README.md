# Squid-sanitize-blacklist
Sanitizes domains in Squid Proxy blacklist files. 
The script takes a text file containing several domains, then sorts and filters so that duplicates entries and subdomains of a parent domain is removed.
The result is a crystal clean domain list that Squid proxy accepts happily.
