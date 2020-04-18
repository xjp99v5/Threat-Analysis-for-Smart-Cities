'''
#Update: standard input interface for this auto-detection kernel
For example, this system consists of Cisco, Oracle, Linux, MS, WebAcess, and, SQL components, defining component,
component = ['Cisco', 'Oracle', 'Linux', 'MS', 'WebAccess', 'SQL']
The vulnerability key-value pair associated with the component is defined as vulnerabilityDict. The key is element corresponding to the element of the above component, 
and the value is the vulnerability related to the component.
For example, vQ is related to Oracle components
vulnerabilityDict ['element'] = Oracle
vulnerabilityDict ['vulnerability'] = vQ, 
and then many component vulnerabilities form a vulnerability array vulVec.
The relationship between other components caused by the vulnerability or the relationship between components is indicated by parentheses (vulVec [3] ['element'], vulVec [4] ['element']), which means that There is an association relationship between the components of vulVec [3] and vulVec [ 4] . For example, vulVec [3] ['element'] is Oracle, and vulVec [4] ['element'] is WebAccess, which means there is a relationship between Oracle and WebAccess.
Three texts or xml need to be entered.
1. System component: component.txt. Each line is a component such as Oracle;
2. Vulnerability corresponding to each component: vulnerabilityDict.txt.  The first column is the component name, the second column is the vulnerability information (the vulnerability information has multiple representations, the second column is the key, for example, the second column is the vulnerability ID, and the third column is the vulnerability Name, the fourth column is the vulnerability risk level, etc.. The vulnerability ID satisfies the uniqueness of the vulnerability);
3. The relationship of each component or vulnerability: vulnerRelationship.txt is also two columns. The first column is the key of the previous component or vulnerability, and the second column is the key of the latter component or vulnerability. The first column of each row is associated with the second column, such as Oracle : WebAccess.
The above three texts can create a database table and directly read the table data.
'''
