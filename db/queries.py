TABLESPACE_USAGE_SQL = """
SELECT d.STATUS "Status",
       d.tablespace_name "Name",
       d.contents "Type",
       d.extent_management "Extent Management",
       d.initial_extent "Initial Extent",
       TO_CHAR(NVL(a.bytes / 1024 / 1024 , 0),'99,999,999.999') "Size (M)",
       TO_CHAR(NVL(a.bytes - NVL(f.bytes, 0), 0)/1024/1024,'99,999,999.999') "Used (MB)",
       TO_CHAR(NVL((a.bytes - NVL(f.bytes, 0)) / a.bytes * 100, 0), '990.00') "Used %",
       TO_CHAR(NVL(a.maxbytes / 1024 / 1024 , 0),'99,999,990.900') "MaxSize (MB)",
       TO_CHAR(NVL((a.bytes - NVL(f.bytes, 0)) / a.maxbytes * 100, 0), '990.00') "Used % of Max"
FROM sys.dba_tablespaces d,
     (SELECT tablespace_name,
             SUM(bytes) bytes,
             SUM(DECODE(autoextensible,'NO',bytes,'YES',maxbytes)) maxbytes
      FROM dba_data_files
      GROUP BY tablespace_name) a,
     (SELECT tablespace_name, SUM(bytes) bytes
      FROM dba_free_space
      GROUP BY tablespace_name) f
WHERE d.tablespace_name = a.tablespace_name(+)
  AND d.tablespace_name = f.tablespace_name(+)
ORDER BY 10 DESC
"""

DATAFILE_SQL = """
SELECT file_id,
       file_name,
       tablespace_name,
       SUM(bytes)/(1024*1024) bytes,
       SUM(maxbytes)/(1024*1024) max,
       autoextensible,
       (SUM(maxbytes)/(1024*1024)) - (SUM(bytes)/(1024*1024)) "Free Space"
FROM dba_data_files
WHERE tablespace_name LIKE :tbls
GROUP BY file_id, file_name, tablespace_name, autoextensible
ORDER BY 1,2,3
"""
