from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

class Survey:
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.location = data['location']
        self.language = data['language']
        self.comments = data['comments']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
    @classmethod
    def save(cls, data):
        print("Entrando a save",data)
        query = "INSERT into surveys (name, location, language, comments) VALUES (%(name)s, %(location)s, %(language)s, %(comments)s)"
        result = connectToMySQL('dojo_survey').query_db(query, data)
        return result
    
    @classmethod
    def get_survey(cls):
        query = "SELECT * FROM surveys ORDER BY surveys.id DESC LIMIT 1;"
        result = connectToMySQL('dojo_survey').query_db(query)
        print("Este es el resultado", result)
        return Survey(result[0])
    
    @staticmethod
    def is_valid(survey):
        is_valid = True
        
        if len(survey['name']) < 3:
            is_valid = False
            print("Fallo el nombre")
            flash("El nombre de ser al menos de 3 caracteres")
            
        if len(survey['location']) < 1:
            is_valid = False
            print("Fallo la ubicacion")
            flash("Elija una ubicación")
            
        if len(survey['language']) < 1:
            is_valid = False
            print("Fallo el idioma")
            flash("Elija un idioma")
            
        if len(survey['comments']) < 3:
            is_valid = False
            print("Fallo el comentario")
            flash("El comentario debe tener al menos 3 caracteres")
        
        return is_valid