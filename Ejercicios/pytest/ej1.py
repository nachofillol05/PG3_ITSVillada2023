def validate_password(password):
    if len(password) > 8:
        if any(chr.isupper() for chr in password):
            if any(chr.islower() for chr in password):
                if any(chr.isdigit() for chr in password):
                    if not any(chr in "!#$%&/()=?'¡¿+*~}]{[^-_.:,;<>|°¬" for chr in password):
                        return True
    return False