def calculate_love_score(name1, name2):
    combined_names = (name1 + name2).lower()


    t_count = combined_names.count('t')
    r_count = combined_names.count('r')
    u_count = combined_names.count('u')
    e_count = combined_names.count('e')
    true_score = t_count + r_count + u_count + e_count

    l_count = combined_names.count('l')
    o_count = combined_names.count('o')
    v_count = combined_names.count('v')
    e_count = combined_names.count('e')  # 'e' appears in both TRUE and LOVE
    love_score = l_count + o_count + v_count + e_count

    love_score_combined = int(str(true_score) + str(love_score))


    print(f"Love Score = {love_score_combined}")

#Test the function
name1 = "Angela Yu"
name2 = "Asish Tony"
calculate_love_score(name1, name2)