[Study]Update Records with same key According No-unique Index, DeadLock detected
========================

Study MySQL Innodb Deadlock

非唯一主键索引相同Key的行发生死锁
========================

报警日志中发现了一个死锁, InnoDB Status显示两个Update语句发生了死锁故障.

此处为对死锁的学习研究.