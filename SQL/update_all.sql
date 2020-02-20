UPDATE salary /*Selects the salary table*/
SET /* use set to set all values*/
    sex = CASE sex /* select the collumns as a case*/
        WHEN 'm' THEN 'f' /* if the column is make then change to female*/
        ELSE 'm'
    END;