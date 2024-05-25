SELECT DISTINCT sub.subject_name
FROM subjects sub
JOIN grades g ON sub.subject_id = g.subject_id
WHERE g.student_id = ?;