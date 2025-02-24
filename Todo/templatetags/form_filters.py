from django import template

register = template.Library()

@register.filter(name='attr')
def attr(field, args):
    if args:
        attrs = dict(item.split(":") for item in args.split(","))
    else:
        attrs = args.split(":")
    field.field.widget.attrs.update(attrs)

    return field
