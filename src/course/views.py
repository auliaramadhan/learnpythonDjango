from django.shortcuts import render, get_object_or_404
from django.views import View
# from .models import Course
from .forms import Course, CourseModelForm

# buat parent buat bikin mehtod get object yang dipakai terus
class CourseObjectMixin(object):
    model = Course
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(self.model, id=id)
        return obj 

class CourseListView(View):
    template_name = 'course/course_list.html'
    queryset = Course.objects.all()

    def get_queryset(self):
        return self.queryset

    def get(self, req, id=None):
        return render(req, self.template_name, {'object_list':self.queryset})

class CourseView(View):
    template_name = 'course/course_detail.html'
    def get(self, req, id=None):
        # get method
        # object = get_object_or_404(Course, id= id)
        context = {'object': self.get_object()}
        return render(req, self.template_name, context)

    # def post(self, req):
    #     # post method
    #     return render(req, 'about.html', {})

class CourseCreateView(View):
    template_name = 'course/course_create.html'
    def get(self, req):
        form = CourseModelForm()
        context = {'form': form}
        return render(req, self.template_name, context)
    def post(self, req):
        form = CourseModelForm(req.POST)
        if form.is_valid():
            form.save()
        context = {'form':form}
        return render(req, self.template_name, context)

class CourseDeleteView(CourseObjectMixin, View):
    template_name = "course/course_delete.html" # DetailView
    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            context['object'] = obj
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            obj.delete()
            context['object'] = None
            return redirect('/course/')
        return render(request, self.template_name, context)


class CourseUpdateView(CourseObjectMixin, View):
    template_name = "course/course_update.html" # DetailView
    def get_object(self):
        id = self.kwargs.get('id')
        obj = None
        if id is not None:
            obj = get_object_or_404(Course, id=id)
        return obj

    def get(self, request, id=None, *args, **kwargs):
        # GET method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(instance=obj)
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)

    def post(self, request, id=None,  *args, **kwargs):
        # POST method
        context = {}
        obj = self.get_object()
        if obj is not None:
            form = CourseModelForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
            context['object'] = obj
            context['form'] = form
        return render(request, self.template_name, context)



# view default biasa
# HTTP method
def my_view(req):
    return render(req, 'about.html', {})

