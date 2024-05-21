from collections import Counter


def baseline_candidates(test_query_rel, edges, obj_dist, rel_obj_dist):

    if test_query_rel in edges:
        candidates = rel_obj_dist[test_query_rel]
    else:
        candidates = obj_dist

    return candidates


def calculate_obj_distribution(learn_data, edges):

    objects = learn_data[:, 2]
    dist = Counter(objects)
    for obj in dist:
        dist[obj] /= len(learn_data)
    obj_dist = {k: round(v, 6) for k, v in dist.items()}
    obj_dist = dict(sorted(obj_dist.items(), key=lambda item: item[1], reverse=True))

    rel_obj_dist = dict()
    for rel in edges:
        objects = edges[rel][:, 2]
        dist = Counter(objects)
        for obj in dist:
            dist[obj] /= len(objects)
        rel_obj_dist[rel] = {k: round(v, 6) for k, v in dist.items()}
        rel_obj_dist[rel] = dict(
            sorted(rel_obj_dist[rel].items(), key=lambda item: item[1], reverse=True)
        )

    return obj_dist, rel_obj_dist
