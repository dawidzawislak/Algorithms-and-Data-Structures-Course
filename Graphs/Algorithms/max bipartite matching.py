def binworker( M ):
    n = len(M)
    matches = [None]*n
    matched_worker = [False]*n

    def find_match(worker, visited_machines):
        nonlocal M, matches
        
        for m in M[worker]:
            if not visited_machines[m]:
                visited_machines[m] = True
                if matches[m] == None or find_match(matches[m], visited_machines):
                    matches[m] = worker
                    return 1
        return 0

    pairs = 0

    for worker in range(n):
        for m in M[worker]:
            if matches[m] == None:
                matches[m] = worker
                matched_worker[worker] = True
                pairs += 1
                break

    for worker in range(n):
        if not matched_worker[worker]:
            visited_machines = [False]*n
            pairs += find_match(worker, visited_machines)

    return pairs