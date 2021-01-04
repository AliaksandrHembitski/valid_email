def valid_email(email):
    if email.count("@") == 1 and "." in email:
        if email[0] != "@" and email[-1] != "@":
            if email[0] != "." and email[-1] != ".":
                l = email.split("@")[-1]
                if ''.join(l.split('.')).isalpha() and l.count('.') >= 1:
                    if l[0] != "." and l.islower():
                        a = 0
                        for i in range(len(l)):
                            if l[i - 1] == "." and l[i] == ".":
                                a += 1
                        if a == 0:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False
    else:
        return False
