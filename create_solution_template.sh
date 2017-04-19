# deletes all files in an user's folder and repopulate based on the shared templates
# please execute this script in its current directory
# eg 'single_number'
PROBLEM=$1
# eg 'gy'
USER=$2

echo "Creating new folder for ${PROBLEM} (if does not already exist)"
mkdir -p ${PROBLEM}

sed "s/PROBLEM/${PROBLEM}/g" template_solution.py > ${PROBLEM}/${PROBLEM}_${USER}.py
sed "s/PROBLEM/${PROBLEM}/g" template_test.py | sed "s/USER/${USER}/g" > ${PROBLEM}/test_${PROBLEM}.py
# sed "s/USER/${USER}/g" ${PROBLEM}/test_${PROBLEM}.py > ${PROBLEM}/test_${PROBLEM}.py
