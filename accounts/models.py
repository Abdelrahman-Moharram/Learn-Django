from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User,BaseUserManager,AbstractBaseUser
import job.models 

















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







def imagesave(instance,filename):
    imagename , extension = filename.split(".")
    return "users/%s/%s/"%(instance.id,"images")

def cap(string):
    new=string[0].upper()
    for i in range(1,len(string),1):
        if string[i-1] == '-':
            new += string[i].upper()
        else:
            new +=string[i]
    return new

class account(AbstractBaseUser):

    choose = (
        ("employeer","you want to hire"),
        ("employee" ,"you want a job")
    )

    fname         = models.CharField(max_length=20,verbose_name="First Name",unique=False)
    lname         = models.CharField(max_length=20,verbose_name="Last Name",unique=False)
    phone         = models.CharField(max_length=12, verbose_name="Phone",unique=True)
    email         = models.EmailField(unique = True, max_length=254)
    password      = models.CharField(max_length=150)
    image         = models.ImageField(default="users/logo.png",upload_to=imagesave, height_field=None, width_field=None)
    joined_at     = models.DateField(auto_now_add=True,verbose_name="joined at")
    slug          = models.SlugField(blank=True,null=True)
    is_admin      = models.BooleanField(default=False)
    is_staff      = models.BooleanField(default=False)
    is_superuser  = models.BooleanField(default=False)
    user_type     = models.CharField(max_length=30)

    USERNAME_FIELD  = 'email'
    REQUIRED_FIELDS = ['fname','lname','phone']

    objects = accountManager()



    def save(self,*args, **kwargs):
        self.slug = slugify(self.fname+" "+self.lname)
        self.slug = cap(self.slug)
        super(account,self).save(*args,**kwargs)


    
    def __str__(self):
        return self.email


    def has_perm(self , perm , obj = None):
        return self.is_admin
    
    def has_module_perms(self,app_label):
        return True

    





class employeer(models.Model):
    user          = models.OneToOneField(account,on_delete=models.CASCADE)
    linkedin    = models.URLField(max_length=200,null=True,blank=True)
    
    def __str__(self):
        return self.user.slug
    


class employee(models.Model):

    exps = (
        ("0-1 year","0-1 year"),
        ("1-3 years","1-3 years"),
        ("3-6 years","3-6 years"),
        ("6+ years","6+ years"),
    )
    user          = models.OneToOneField(account,on_delete=models.CASCADE)
    cv            = models.FileField(upload_to="users/data/", max_length=100)
    start_salary  = models.IntegerField(verbose_name="start salary")
    categery      = models.ManyToManyField("job.Category")
    exp           = models.CharField( max_length=50,choices=exps)
    linkedin      = models.URLField(max_length=200,null=True,blank=True)
    github        = models.URLField(max_length=200,null=True,blank=True)

    def __str__(self):
        return self.user.slug
    




