.. _appendbackslash:

====================
Cog: AppendBackslash
====================

-------
Outline
-------

:code:`AppendBackslash` is a cog that ultimately allows you to append backslashes to the start of any given string.
This can be useful for those who don't have backslashes on their keyboard, or if you want to get a raw version of an emoji.

------------
Installation
------------

Make sure you have :code:`Downloader` loaded!

:code:`[p]load Downloader`

Let's add Kreusada's repository firstly:

:code:`[p]repo add kreusadacogs https://github.com/kreus7/kreusadacogs`

Now, you can add the :code:`AppendBackslash` cog into your system.

:code:`[p]cog install kreusadacogs appendbackslash`

-----
Usage
-----

- :code:`[p]abs <object_to_append>`

No, :code:`abs` doesn't get you abdominals, it stands for append backslash. Sorry about that guys.

-------------
Example Usage
-------------

- :code:`[p]abs n`

.. code-block:: bash

    \n
    
- :code:`[p]abs :white_check_mark:`

.. code-block:: bash

    ✅
    
-----------
Emoji Usage
-----------

When you backslash an emoji, you convert the emoji into it's raw form, meaning that you can paste this emoji rather than its 'colon'ed equivalent.
You will be able to notice the difference below:

.. code-block:: python

    await ctx.message.add_reaction("✅")
    await ctx.send("✅")
    
.. code-block:: python

    await ctx.message.add_reaction(":white_check_mark:")
    await ctx.send(":white_check_mark:")

-------
Support
-------

As always, you can join my `support server <https://discord.gg/JmCFyq7>`_ if you need help!

- Kreusada
