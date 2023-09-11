import scipy.stats as stats


# Sample data
data1 = [70,7]
data2 = [104,24]

# Perform an independent two-sample t-test
t_statistic, p_value = stats.ttest_ind(data1, data2, equal_var=False)

# Print the results
print("T-statistic:", t_statistic)
print("P-value:", p_value)

# Interpret the results
alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: The means are significantly different.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in means.")
    
    #השערת האפס היא שהם שונים
    #תוצאה- ההבדל לא משמעותי בין התוחלות- 
    #  האם אפשר להסתייג ולמרות זאת לכתוב ההבדלים לא שונים משמעותית אך כן נראה שיש הבדל?
    #כדי שתהיה מסקנה