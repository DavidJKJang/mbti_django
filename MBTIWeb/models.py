from django.db import models


class TeamMBTI(models.Model):
	teamId = models.AutoField(primary_key=True)
	teamName = models.CharField(max_length=10)
	teamAddress = models.CharField(max_length=10)
	createTime = models.DateTimeField()


class TeamMember(models.Model):
	MBTICase = [
		('ENTJ', 'ENTJ'),
		('ENTP', 'ENTP'),
		('INTJ', 'INTJ'),
		('INTP', 'INTP'),
		('ESTJ', 'ESTJ'),
		('ESFJ', 'ESFJ'),
		('ISTJ', 'ISTJ'),
		('ISFJ', 'ISFJ'),
		('ENFJ', 'ENFJ'),
		('ENFP', 'ENFP'),
		('INFJ', 'INFJ'),
		('INFP', 'INFP'),
		('ESTP', 'ESTP'),
		('ESFP', 'ESFP'),
		('ISTP', 'ISTP'),
		('ISFP', 'ISFP')
	]
	memberId = models.AutoField(primary_key=True)
	memberName = models.CharField(max_length=10)
	MBTI = models.CharField(max_length=4, choices=MBTICase)
	teamId = models.ForeignKey(TeamMBTI, default=1, on_delete=models.CASCADE)
	memberJoinDate = models.DateTimeField()
