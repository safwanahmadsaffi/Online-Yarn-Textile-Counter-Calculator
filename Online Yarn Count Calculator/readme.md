<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Online Yarn Count Calculation Guide for Textile</title>
    <style>
        body {font-family: Arial, sans-serif; line-height: 1.6; margin: 40px;}
        h1 {color: #2c3e50; border-bottom: 2px solid #3498db;}
        h2 {color: #34495e;}
        table {border-collapse: collapse; margin: 25px 0; width: 100%;}
        th, td {border: 1px solid #ddd; padding: 12px; text-align: left;}
        th {background-color: #3498db; color: white;}
        tr:nth-child(even) {background-color: #f2f2f2;}
        .formula {background-color: #f9f9f9; padding: 15px; margin: 15px 0; border-left: 4px solid #3498db;}
        .example {background-color: #e8f4f8; padding: 15px; margin: 15px 0; border-radius: 5px;}
    </style>
</head>
<body>
    <h1>How to Use: Different Length and Weight Units Used in Important Indirect Systems</h1>

    <h2>Indirect Systems Table</h2>
    <table>
        <tr>
            <th>Name of System</th>
            <th>Unit of Weight</th>
            <th>Unit of Length</th>
        </tr>
        <tr><td>English Cotton</td><td>1 lb</td><td>Hank of 840 yards</td></tr>
        <tr><td>French Cotton</td><td>1 kg</td><td>Hank of 1000 meters</td></tr>
        <tr><td>Bump Cotton</td><td>1 oz</td><td>1 yard</td></tr>
        <tr><td>Decimal (for all yarns)</td><td>1 lb</td><td>Hank of 1000 yards</td></tr>
        <tr><td>Metric</td><td>1 kg</td><td>Hank of 1000 meters</td></tr>
        <tr><td>Spun Silk</td><td>1 lb</td><td>Hank of 840 yards</td></tr>
        <tr><td>Spun rayon staple fibers</td><td>1 lb</td><td>Hank of 840 yards</td></tr>
        <tr><td>Worsted</td><td>1 lb</td><td>Hank of 560 yards</td></tr>
        <tr><td>Linen (Wet spun)</td><td>1 lb</td><td>Lea of 300 yards</td></tr>
        <tr><td>Hemp (fine)</td><td>1 lb</td><td>Lea of 300 yards</td></tr>
        <tr><td>Woolen- Yorkshire Skein</td><td>6 lbs</td><td>Skein of 1536 yards</td></tr>
        <tr><td>Woolen- American Cut</td><td>1 lb</td><td>Cut of 300 yards</td></tr>
        <tr><td>Woolen- American Run</td><td>1 oz</td><td>Run of 100 yards</td></tr>
        <tr><td>Woolen- Dewsbury</td><td>1 oz</td><td>1 yard</td></tr>
        <tr><td>Woolen- Hawick</td><td>26 ozs</td><td>Cut of 300 yards</td></tr>
        <tr><td>Woolen- Galashiels</td><td>24 ozs</td><td>Cut of 300 yards</td></tr>
        <tr><td>Woolen- Alloa</td><td>24 lbs</td><td>Spyndle of 11520 yards</td></tr>
        <tr><td>Woolen-West of England</td><td>1 lb</td><td>Snap of 320 yards</td></tr>
        <tr><td>Asbestos- British</td><td>1 lb</td><td>Hank of 50 yards</td></tr>
        <tr><td>Asbestos – American</td><td>1 lb</td><td>Cut of 100 yards</td></tr>
        <tr><td>Fiber Glass</td><td>1 lb</td><td>100 yards</td></tr>
    </table>

    <h2>Calculation Formulas</h2>
    <div class="formula">
        <h3>Indirect System Formula</h3>
        <pre>
Count = Number of length units per weight unit

        Length in appropriate length unit
Count = -------------------------------------
        Weight in corresponding Weight Unit
        </pre>
    </div>

    <div class="formula">
        <h3>Direct System Formula</h3>
        <pre>
        Weight in Appropriate unit
Count = ---------------------------
        Length in Appropriate unit
        </pre>
    </div>

    <h2>Examples</h2>
    <div class="example">
        <h3>Indirect System Example</h3>
        <p>If 240 yards of cotton yarn weight 40 grains:</p>
        <pre>
240 yards = 240/840 hanks
40 grains = 40/7000 lbs

Count = (240/840) / (40/7000) = 50's Cotton
        </pre>
    </div>

    <div class="example">
        <h3>Direct System Example</h3>
        <pre>
Denier System:
Weight = 0.05g, Length = 450m

Count = 9000 × (Weight in grams / Length in meters)
       = 9000 × (0.05/450) = 1 Denier
        </pre>
    </div>

</body>
</html>