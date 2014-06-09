from django.db import models

class Record(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30,verbose_name="书名")
    writer = models.CharField(max_length=10, verbose_name="作者")
    nation = models.CharField(max_length=10, verbose_name="国家/朝代")
    content = models.TextField(verbose_name="内容")
    add_time = models.DateTimeField(verbose_name="添加时间")
    class Meta:
        db_table = "Record"
    def __unicode__(self):
        return self.title
