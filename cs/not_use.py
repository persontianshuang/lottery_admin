
def urd(uid,p3,p2):
    ur = UserRecommend()
    ur.uid = uid
    # ur.p1 = '1'
    if p2:
        ur.p2 = p2
    ur.p3 = p3
    ur.p4 = 124
    ur.save()
r41 = ['38']
r42 = ['122']
# for u in User.objects.all():
#     # u.uid
#     # u.role
#     if float(u.uid)<60:
#
#         if u.role==5:
#             urd(u.uid,125, random.choice(r41))
#         else:
#             urd(u.uid,125, None)
#             r41.append(u.uid)
#
#     else:
#
#         if u.role == 5:
#             urd(u.uid,126, random.choice(r42))
#         else:
#             urd(u.uid, 126, None)
#             r42.append(u.uid)
#
#     print(u.uid,u.role)
    # u.save()
