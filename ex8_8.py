from collections import Counter


def get_count_visits_from_ip(ips):
    return Counter(ips)
    


def get_frequent_visit_from_ip(ips):
    ip_counts=Counter(ips)
    return list(ip_counts.most_common(1))


ips=[1,2,3,5,3,5,1,2,2,]
print(get_count_visits_from_ip(ips))
print(get_frequent_visit_from_ip(ips))
