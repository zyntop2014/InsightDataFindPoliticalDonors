This test has been provided for you so that you can see one example, however, you should be creating your own tests to check that your code runs as expected.

This test suit is used to test that when TRANSACTION_DATE is not valid, the corresponding records will not be included in the results of medianvals_by_zip.txt but completely ignore the record when calculating values for medianvals_by_date.txt.

The invalid dates include an empty date, an invalid date in digit(such as 01402017), invalid dates in length (such as 0107 or 12343433), invalid dates with other charters (01jun2017) etc.
