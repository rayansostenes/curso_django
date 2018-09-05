class BaseModel(models.Model):
    class Meta:
        abstract = True
        managed = False
    
    SQL_QUERY = None

    def get_values(self):
        raise NotImplementedError

    def save(self):
        with connection.cursor() as cur:
            cur.execute(self.SQL_QUERY, self.get_values)

    

class Modelo(BaseModel):

    SQL_QUERY = '''
        INSERT INTO table_name (coluna1, coluna2) VALUES (%s, %s)
    '''
    coluna1 = models.IntegerField()
    coluna2 = models.IntegerField()

    def get_values(self):
        return [
            self.coluna1,
            self.coluna2
        ]