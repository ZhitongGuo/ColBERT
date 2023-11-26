def get_windowed_obs(obs, query, indexer, adj=10, set_k_adj=1, set_k_bound=5):
    obs_list = obs.split("\n")

    results = query_html(obs_list, query, indexer, k=max(set_k_adj, set_k_bound))
    results.sort(key=lambda x: obs_list.index(x))

    output_adj = OrderedSet()
    for res in results[:set_k_adj]:
        top_element_index = obs_list.index(res)
        start = max(top_element_index-adj, 0)
        end = min(top_element_index+adj, len(obs_list))
        windowed_obs_adj = obs_list[start:end]
        for item in windowed_obs_adj:
            output_adj.add(item)

    top_element_index_bound = obs_list.index(results[0])
    bottom_element_index_bound = obs_list.index(results[-1]) + 1
    windowed_obs_bound = obs_list[top_element_index_bound:bottom_element_index_bound]

    return results[:set_k_adj], list(output_adj), windowed_obs_bound