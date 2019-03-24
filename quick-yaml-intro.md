# Quick YAML Intro

There is only a subset of YAML that is used for the kit specification file. These are:

## Beginning a YAML file

Always begin a file with:

```yaml
---
```

## Key Value Pairs

The specification file has a number of special keywords and associated values.
These usually look something like:

```yaml
name: Grunt clothing
```

where `name` is a **keyword** and `Grunt clothing` is a **value**.
In this case the value is a **string**.

## Value Types

### String

This can be any arbitrary text, and is the default value type when you just have a word, sentence or non number. You can force a value to be a String by enclosing it with `"`, for example `"[SL]"` needs those, otherwise YAML may interpret the `[` and `]` symbols as donoting an array.

### Number

Any positive, negative or decimal number, like for example, `1`, `1.1`, or `-1.1`.

### Object

A collections of **Key Value Pairs**, where each key is unique. For example, here is an object:

```yaml
type: HandGrenade
count: 4
```

Objects are sometimes also called **hashes** and **dictionaries**.

### Array

Also called a **List**, it's a series of values of any type, with each separate element prefixed by a `-` symbol. In the case of the ZAKM, they will always be **Strings** or **Objects**.

For example, here is an array of strings:

```yaml
- farkhar
- mcn_aliabad
- clafghan
- desert_e
```

When using an array as a value, make sure to indent the array correctly, like so:

```yaml
worlds:
  - farkhar
  - mcn_aliabad
  - clafghan
  - desert_e
```

Here is an array of 3 objects, where each object has 2 keys (`type` and `count`):

```yaml
- type: HandGrenade
  count: 4
- type: ACE_M84
  count: 2
- type: SmokeShell
  count: 8
```

As hinted at earlier, another way of writing an array is by putting all the elemets in between `[` and `]`, separating each element with `,` like so:

```yaml
[farkhar, mcn_aliabad, clafghan, desert_e]
```

## Nested Key Value Pairs (or objects)

Because a value can be an object, this means that you can nest any level of objects, each having any value types. For example:

```yaml
visibility_conditions:
  - name: Night
  - name: Day
```

The key `visibility_conditions` has as it's value an array of two objects, where each object consits of one key value pair, where those keys are `name`.

Here is a more complex example, where again, the top level key `kit_collections` has as it's value, an array of objects, but this time those objects have differing values including their own array of objects, thus giving us **Nested objects**.

```yaml
kit_collections:
  - name: Grunt clothing
    goggles:
      - type: G_Combat
    headgear:
      - type: H_HelmetSpecB_paint2
        terrain_conditions:
          - Arid
  - name: Peronal radio
    miscelaneous:
      - type: ACRE_PRC343
```
