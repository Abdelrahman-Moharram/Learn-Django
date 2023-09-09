from django.db import models
from django.contrib.auth.models import User,BaseUserManager,AbstractBaseUser
from django.utils.text import slugify



def imagesave(instance,filename):
    imagename , extension = filename.split(".")
    return "users/%s/%s/"%(instance.id,"images", extension)



def cap(string):
    new=string[0].upper()
    for i in range(1,len(string),1):
        if string[i-1] == '-':
            new += string[i].upper()
        else:
            new +=string[i]
    return new


class accountManager(BaseUserManager):
    def create_user(self,email,fname,lname,phone,password = None):
        if not email:
            raise ValueError('user must have an email')

        if not fname:
            raise ValueError('Unvalid Null Value')
        
        if not lname:
            raise ValueError('Unvalid Null Value')
        
        if not phone:
            raise ValueError('Unvalid Null Value')
        
        user = self.model(
            email = self.normalize_email(email),
            phone = phone,
            fname = fname,
            lname = lname
        )

        user.set_password(password)
        user.save(using = self._db)
        return user
    

    def create_superuser(self,email,fname,lname,phone,password):
        user = self.create_user(
            email = self.normalize_email(email),
            phone = phone,
            fname = fname,
            lname = lname,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        
        return user 





class User(AbstractBaseUser):
    
    fname         = models.CharField(max_length=20,verbose_name="الاسم الاول",unique=False)
    lname         = models.CharField(max_length=20,verbose_name="الاسم الاخير",unique=False)
    phone         = models.CharField(max_length=12, verbose_name="رقم الهاتف",unique=True)
    email         = models.EmailField(unique = True, max_length=254)
    password      = models.CharField(max_length=150)
    # image         = models.ImageField(default="users/logo.png",upload_to=imagesave, null=True, height_field=None, width_field=None)
    joined_at     = models.DateField(auto_now_add=True,verbose_name="تاريخ الانضمام")
    username      = models.SlugField(blank=True,null=True)
    is_admin      = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['fname','lname','phone']

    objects = accountManager()



    def save(self,*args, **kwargs):
        self.username = slugify(self.fname+"-"+self.lname)
        self.username = cap(self.username)
        super(User,self).save(*args,**kwargs)


    
    def __str__(self):
        return self.username or self.email


    def has_perm(self , perm , obj = None): # to not access admin panel
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True

    
