# Localization

Program localization system.

Any language you want can be added.

Currently the system is set up for:

* Bulgarian
* English
* Romanian

## Localization of the program

The program uses standard .po and .mo files.
In case you want to localize in your own language, open the .po file.

We recommend using a .po editor such as [poedit](https://poedit.net/) which will simplify the translation work.
and generating a .mo file.

You can always correct an existing language, but it is advisable to send the translation to

<a href="mailto:grigor.kolev@gmail.com"> Grigor Kolev </a> to be integrated into the system.

If the translation is not integrated, it is likely to be overwritten and / or not received
new updates messages.

.po files can be corrected with any text editor by correcting __msgstr__

```buildoutcfg
msgid "User"
msgid "User"
```

.po and .mo files are located in colibri/locale/

## Change print documents

The documents are an html file with integrated [jinja2](https://jinja.palletsprojects.com/en/2.11.x/templates/).

Fix them the way you want them to look.

All printing documents are in

colibri/template

Please send changes to

<a href="mailto:grigor.kolev@gmail.com"> Grigor Kolev </a> to be integrated into the system.

If they are not integrated, they are likely to be overwritten and/or not received
new changes when updating.


## Localization of the documentation

All documentation is on [markdown](https://www.markdownguide.org/basic-syntax/) the site is generated automatically.

If you want to make changes, contact

<a href="mailto:grigor.kolev@gmail.com"> Grigor Kolev </a>