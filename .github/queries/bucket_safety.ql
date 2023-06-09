/**
 * @name Bucket Safety
 * @description User-controlled variable used as bucket
 * @kind problem
 * @problem.severity recommendation
 * @sub-severity high
 * @precision very-high
 * @id py/bucket-safety
 */

import python

from Function f
where f.getName() = "api_method"
select f,1