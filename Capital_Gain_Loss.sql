SELECT 
stock_name,
SUM (
    CASE 
        WHEN operation = 'Buy' THEN -price
        ELSE price
    END
    ) 
AS capital_gain_loss
FROM Stocks s1
GROUP BY stock_name;

SELECT 
stock_name,
SUM (
    IF(operation = 'Sell', price, -price)
    )
AS capital_gain_loss
FROM Stocks s1
GROUP BY stock_name;