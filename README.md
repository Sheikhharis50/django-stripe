# django-stripe

> By Sheikh Haris Zahid

`Project` have some sub-apps:

- `app_core` - (which has core fucntionalities of project.)
- `app_order` - (in which we store orders according to the user subscription.)
- `app_subscription` - (in which we can create subscriptions and user can subscribe a subscription after paying for it.)

`Project` has some constraints which we need to follow:

- user must have a subscription to create an order.
- user can have only one subscription at a time.
- subscription considered to be end, when `ordered` field is equal to `can_order` field.
