from scipy.stats import fisher_exact

# Create a contingency table (2x2 table)
# Example: Association between treatment (A/B) and recovery (Yes/No)
#         | Treatment A | Treatment B |
# ------------------------------------
# Recovery|    20       |    10       |
#         |---------------------------------
# No Recov|    30       |    40       |

contingency_table = [[70, 7],
                     [104, 24]]

# Perform Fisher's exact test
odds_ratio, p_value = fisher_exact(contingency_table)

print("Odds Ratio:", odds_ratio)
print("P-Value:", p_value)


alpha = 0.05  # Significance level
if p_value < alpha:
    print("Reject the null hypothesis: The means are significantly different.")
else:
    print("Fail to reject the null hypothesis: There is no significant difference in means.")




