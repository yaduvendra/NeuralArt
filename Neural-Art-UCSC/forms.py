from flask_wtf import Form
from wtforms import StringField, SelectField, SubmitField

class ArtForm(Form):
    user_image = SelectField(u'Main Image', choices=[('taipei101.jpg', "taipei101"), ('cowell.jpg', "cowell"), ('ucsc.jpg', "ucsc")])
    checkpoint = SelectField(u'Artist Stlye', choices=[('la_muse.ckpt', "La Muse"),
                                                       ('rain_princess.ckpt', "Rain Princess"),
                                                       ('scream.ckpt', "The Scream"),
                                                       ('wreck.ckpt', "The Shipwreck"),
                                                       ('udnie.ckpt', "Udnie"),
                                                       ('wave.ckpt', "Wave")
                                                      ])
    endpoint = StringField('Endpoint')

############################### Modifications #########################
    urlName = StringField('Image Name')
    urlLink = StringField('Image Link')
############################### End Modifications #########################s
    submit = SubmitField("Generate Art")
