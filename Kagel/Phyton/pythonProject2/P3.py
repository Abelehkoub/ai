flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"
print(flowers.split(","))

test_ratings = [1, 2, 3, 4, 5]
test_liked = [i>=4 for i in test_ratings]
print(test_liked)

def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    # TODO: Complete the function
    percentage_liked = sum(list_liked) /8
    print(percentage_liked)
    print(list_liked)
    return percentage_liked

# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])
def percentage_liked(ratings):
    list_liked = [i>=4 for i in ratings]
    # TODO: Complete the function
    percentage_liked = sum(list_liked) / 8
    print(percentage_liked)

    return percentage_liked



# Do not change: should return 0.5
percentage_liked([1, 2, 3, 4, 5, 4, 5, 1])

def percentage_growth(num_users, yrs_ago):
    print(num_users[len(num_users)-1])
    print(num_users[len(num_users) - yrs_ago-1])
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
    return growth

# Do not change: Variable for calculating some test examples
num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]

# Do not change: Should return .036
print(percentage_growth(num_users_test, 1))

# Do not change: Should return 0.66
print(percentage_growth(num_users_test, 7))


#