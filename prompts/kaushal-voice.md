# Kaushal Voice prompts

Use these prompts when you want the output to follow the `kaushal-voice` profile.

## General professional rewrite

```text
Use dsc-humanizer.

mode: kaushal-voice
strength: medium
audience: professional
length: same

Rewrite:
[paste draft]
```

## Donor / CSR report

```text
Use dsc-humanizer.

mode: kaushal-voice
strength: medium
audience: donor / CSR partner
priority: evidence, scale, outcome, implementation quality, next step
preserve_terms: [add project-specific technical terms]

Rewrite:
[paste draft]
```

## Technical note

```text
Use dsc-humanizer.

mode: kaushal-voice
strength: medium
audience: technical team
priority: method, assumptions, measurement, field conditions, limitations

Rewrite:
[paste draft]
```

## Donor observation / compliance response

```text
Use dsc-humanizer.

mode: kaushal-voice
strength: medium
audience: donor / reviewer
response_type: observation-response
priority: acknowledge valid gap, explain evidence, distinguish documentation from technical issue where justified, state corrective action

Rewrite:
[paste observation and draft response]
```

## Governing Board note

```text
Use dsc-humanizer.

mode: kaushal-voice
strength: medium
audience: Governing Board
priority: programme direction, field evidence, institutional progress, risks, convergence, decisions and next steps
length: concise

Rewrite:
[paste draft]
```

## Useful optional controls

```text
length: same | shorter | X words
preserve_terms: [...]
must_keep: [...]
strength: light | medium | deep
```

The core rule still applies: **style may change; facts must not.**
