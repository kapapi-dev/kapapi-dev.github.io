"""Page bodies for build.py. One entry per generated page."""

CLEANPASTE_TERMS = """
  <p class="eyebrow">CleanPaste</p>
  <h1 style="font-size:clamp(2rem,5vw,2.8rem)">Terms of service</h1>
  <p style="color:var(--ink-muted)">Last updated: 1 September 2026</p>

  <h2>The agreement</h2>
  <p>These terms cover your use of CleanPaste, a Google Docs editor add-on published by KaPaPi.
  By installing or using it you accept them. If you do not, do not install it.</p>

  <h2>What you get</h2>
  <p>CleanPaste is provided free of charge. There is no trial, no paid tier, no subscription and no
  payment of any kind. You may use it for personal or commercial work.</p>

  <h2>What it does to your documents</h2>
  <p>CleanPaste edits the Google Doc you run it in: it deletes characters it identifies as surplus,
  removes surplus empty paragraphs, and merges paragraphs it identifies as parts of one wrapped
  line. It is designed to be conservative and refuses to act where it cannot act safely, but
  <strong>it does change your document</strong>, and that is the point of it.</p>
  <p>Google Docs keeps a full version history, and Ctrl+Z (Cmd+Z on Mac) undoes a clean in one step.
  Please satisfy yourself with the result before relying on it. You remain responsible for your own
  documents and their backups.</p>

  <h2>No warranty</h2>
  <p>CleanPaste is provided &ldquo;as is&rdquo;, without warranty of any kind, express or implied,
  including but not limited to the warranties of merchantability, fitness for a particular purpose
  and non-infringement. It is not guaranteed to be uninterrupted, error-free, or to produce any
  particular result in any particular document.</p>

  <h2>Limitation of liability</h2>
  <p>To the fullest extent permitted by law, the developer is not liable for any claim, damages or
  other liability &mdash; including loss of data, loss of profit, or consequential loss &mdash;
  arising from or in connection with CleanPaste or its use.</p>
  <p>Nothing in these terms limits any liability that cannot be limited under the law that applies
  to you, including your statutory rights as a consumer.</p>

  <h2>Your data</h2>
  <p>CleanPaste collects nothing, transmits nothing and stores nothing. See the
  <a href="/cleanpaste/privacy.html">privacy policy</a> for the detail.</p>

  <h2>Source code and licence</h2>
  <p>CleanPaste&rsquo;s source is public at
  <a href="https://github.com/kapapi-dev/cleanpaste">github.com/kapapi-dev/cleanpaste</a> and is
  licensed under the MIT Licence. Those licence terms govern the source code; these terms govern the
  hosted add-on you install from the Google Workspace Marketplace.</p>

  <h2>Availability and changes</h2>
  <p>CleanPaste may be changed, suspended or withdrawn at any time. Material changes to these terms
  will be published on this page with a new date above. Continuing to use CleanPaste after a change
  means you accept the revised terms.</p>

  <h2>Ending it</h2>
  <p>You may stop using CleanPaste at any time by uninstalling it from the Google Workspace
  Marketplace or from <strong>Extensions &rarr; Add-ons &rarr; Manage add-ons</strong> in Google
  Docs. Uninstalling removes its access immediately.</p>

  <h2>Governing law</h2>
  <p>These terms are governed by the laws of the Republic of Korea, without regard to conflict of
  law rules, and without depriving you of the protection of any mandatory consumer law that applies
  where you live.</p>

  <h2>Contact</h2>
  <p><a href="mailto:support@kapapi.dev">support@kapapi.dev</a></p>
"""

CLEANPASTE_SUPPORT = """
  <p class="eyebrow">CleanPaste</p>
  <h1 style="font-size:clamp(2rem,5vw,2.8rem)">Support</h1>
  <p class="lead">How to use it, what it deliberately will not do, and how to report a problem.</p>

  <h2>Getting started</h2>
  <ol>
    <li>Install CleanPaste from the Google Workspace Marketplace.</li>
    <li>Open a Google Doc and paste the text you want to tidy.</li>
    <li>Choose <strong>Extensions &rarr; CleanPaste &rarr; Clean document</strong>, or select some
        text first and choose <strong>Clean selection</strong>.</li>
  </ol>
  <p>To choose which cleanups run, open <strong>Extensions &rarr; CleanPaste &rarr; Cleanup
  options&hellip;</strong>. Your choices are remembered in your own browser.</p>

  <h2>Undoing a clean</h2>
  <p>Press <strong>Ctrl+Z</strong> (<strong>Cmd+Z</strong> on Mac). A clean undoes in a single step.
  Google Docs also keeps a full version history under <strong>File &rarr; Version history</strong>.</p>

  <h2>Common questions</h2>

  <h3>It joined two lines that should have stayed apart</h3>
  <p>CleanPaste joins two lines only when the first is at least 30 characters, does not end on
  closing punctuation, and neither line looks like a heading or a list item. Two consecutive
  paragraphs that both end without punctuation match that pattern, because that is exactly what a
  PDF paste looks like.</p>
  <p>Press Ctrl+Z, then untick <strong>Broken line breaks</strong> in the options panel and clean
  again.</p>

  <h3>It did not join lines that clearly belong together</h3>
  <p>The most common reason is that the first line ends in a full stop. CleanPaste never joins after
  one: from the characters alone, a sentence that ends at the end of a line is indistinguishable
  from a paragraph that ends there, and merging two real paragraphs is a much worse mistake than
  leaving a break you can delete yourself.</p>
  <p>Short lines are also never joined &mdash; a line under 30 characters is usually short on purpose.</p>

  <h3>My indented code lost its indentation</h3>
  <p>Leading whitespace is removed as part of <strong>Spacing</strong>, which is right for pasted
  prose and wrong for pasted code. Press Ctrl+Z, untick Spacing, and clean again.</p>

  <h3>Nothing happened inside my table</h3>
  <p>Inside a table cell, only spacing and hidden characters are cleaned. Blank lines and broken line
  breaks are left alone, because a cell is narrow enough that a deliberate line break looks exactly
  like a wrapped one, and reshaping your table on that evidence is not worth the risk.</p>

  <h3>The menu does not appear</h3>
  <p>Reload the document. Editor add-ons attach their menu when a document opens, so a document that
  was already open when you installed CleanPaste needs a refresh.</p>

  <h3>Can I use it on my phone or tablet?</h3>
  <p>No. Google Docs editor add-ons run in the desktop browser only; Google does not support them in
  the Docs mobile apps. This is a platform limitation, not a CleanPaste one.</p>

  <h3>Does my text get uploaded anywhere?</h3>
  <p>No. CleanPaste makes no network requests at all &mdash; no server, no analytics, no AI service.
  It can only see the document it is open in. See the
  <a href="/cleanpaste/privacy.html">privacy policy</a>.</p>

  <h3>Is it really free?</h3>
  <p>Yes. No trial, no upgrade prompt, no paid tier. The source code is public.</p>

  <h2>Reporting a problem</h2>
  <p>The most useful report says what you pasted, what you expected, and what CleanPaste did instead.
  A small before-and-after example is worth more than a description.</p>
  <ul>
    <li><strong>Open an issue:</strong>
        <a href="https://github.com/kapapi-dev/cleanpaste/issues">github.com/kapapi-dev/cleanpaste/issues</a></li>
    <li><strong>Email:</strong> <a href="mailto:support@kapapi.dev">support@kapapi.dev</a></li>
  </ul>
  <p>Please do not paste confidential document content into a public issue.</p>
"""

SORTDOC_INDEX = """
  <p class="eyebrow" style="color:var(--sortdoc)">A KaPaPi tool for Google Docs</p>
  <h1 style="font-size:clamp(2.2rem,5.5vw,3.2rem)">SortDoc</h1>
  <p class="lead">
    <strong>SortDoc is a Google Docs add-on that sorts the paragraphs or list items you have
    selected</strong>, A&nbsp;to&nbsp;Z or Z&nbsp;to&nbsp;A, without flattening their formatting.
  </p>

  <div class="demo">
    <pre>Banana
Apple
Cherry</pre>
    <span class="arrow" aria-hidden="true">&rarr;</span>
    <pre>Apple
Banana
Cherry</pre>
  </div>

  <p>Select the lines you want in order, then choose
  <strong>Extensions &rarr; SortDoc &rarr; Sort A &rarr; Z</strong>. That is the whole product.</p>

  <h2>Formatting moves with the line</h2>
  <p>Most sorting tools read your lines out as plain text, sort the strings and type them back,
  which is why bold, links, headings and bullets tend to disappear. SortDoc reorders the document
  <em>elements</em> instead, so each line carries its own formatting with it.</p>

  <h2>Sort rules</h2>
  <table>
    <tr><th>Rule</th><th>Behaviour</th></tr>
    <tr><td>Case</td><td>Ignored when comparing (<code>banana</code> and <code>Banana</code> are equal)</td></tr>
    <tr><td>Leading/trailing whitespace</td><td>Ignored when comparing; <strong>never removed from the document</strong></td></tr>
    <tr><td>Comparison</td><td><code>localeCompare</code>, so accented and non-Latin text orders sensibly</td></tr>
    <tr><td>Equal values</td><td>Keep their original relative order, in both directions (stable)</td></tr>
    <tr><td>Empty paragraphs</td><td>Sort first A&rarr;Z, last Z&rarr;A</td></tr>
    <tr><td>Numbers</td><td>Compared as text, so <code>10</code> sorts before <code>9</code></td></tr>
  </table>

  <div class="note">
    <p>If SortDoc cannot sort a selection safely, it changes nothing and says so. Refusing is
    always preferred over risking the document.</p>
  </div>

  <h2>Permissions</h2>
  <table>
    <tr><th>Permission</th><th>Why</th></tr>
    <tr><td><code>documents.currentonly</code></td><td>Read and edit <strong>only the document it is open in</strong>. Not Drive, not your other documents</td></tr>
    <tr><td><code>script.container.ui</code></td><td>Draw its menu and messages inside Google Docs</td></tr>
  </table>
  <p>SortDoc makes no network requests. Nothing about your document is sent anywhere, stored
  anywhere, or logged. Full detail in the <a href="/sortdoc/privacy.html">privacy policy</a>.</p>

  <h2>Good to know</h2>
  <ul>
    <li>Sorting is whole-block: it reorders the paragraphs you selected, it does not reorder words
    inside a paragraph.</li>
    <li>The selection must be a run of consecutive paragraphs or list items in the same part of the
    document. Anything else is refused rather than guessed at.</li>
    <li>Editor add-ons run on desktop only; Google does not support them in the Docs mobile apps.</li>
  </ul>
  <p>SortDoc is free. The source is public at
  <a href="https://github.com/kapapi-dev/sortdoc">github.com/kapapi-dev/sortdoc</a>.</p>
"""

SORTDOC_PRIVACY = """
  <p class="eyebrow">SortDoc</p>
  <h1 style="font-size:clamp(2rem,5vw,2.8rem)">Privacy policy</h1>
  <p style="color:var(--ink-muted)">Last updated: 1 September 2026</p>

  <div class="note">
    <p>SortDoc does not collect, transmit, store or share anything. There is no server, no
    database, no analytics, no account and no AI service.</p>
  </div>

  <h2>What SortDoc can see</h2>
  <table>
    <tr><th>Scope</th><th>What it grants</th></tr>
    <tr><td><code>documents.currentonly</code></td>
    <td>The ability to view and manage <strong>the one document the add-on is open in</strong>. It
    does not grant access to Google Drive, to your other documents, or to any file you have not
    opened SortDoc in.</td></tr>
    <tr><td><code>script.container.ui</code></td>
    <td>The ability to draw the add-on&rsquo;s menu and messages inside Google Docs. It does not
    grant access to document content.</td></tr>
  </table>
  <p>Inside that document, SortDoc reads the text of the blocks you selected, reduces each to a
  comparison key in memory, and uses those keys to decide an order. Then it reorders the elements.
  That is the entire data flow.</p>

  <h2>Scopes Google adds by itself</h2>
  <p>Any Google Workspace Marketplace listing automatically includes <code>userinfo.email</code>,
  <code>userinfo.profile</code> and <code>openid</code>. These are attached by the platform and
  cannot be removed from the listing. <strong>SortDoc&rsquo;s own code never calls any identity API
  and never reads your email address, name or profile.</strong></p>

  <h2>No network requests, no analytics</h2>
  <p>SortDoc makes no outbound requests of any kind. It does not use <code>UrlFetchApp</code>, it
  loads no third-party scripts, and it contacts no API. It measures no usage: no counters, no
  events, no crash reporting, no telemetry.</p>

  <h2>Children</h2>
  <p>SortDoc is a general-purpose document utility with no accounts and no data collection. It is
  not directed at children and collects nothing from anyone.</p>

  <h2>Changes to this policy</h2>
  <p>This policy describes the code. If the code&rsquo;s data handling ever changes, this page
  changes in the same commit, and the date above changes with it.</p>

  <h2>Removing SortDoc</h2>
  <p>Uninstall it from the Google Workspace Marketplace, or from <strong>Extensions &rarr; Add-ons
  &rarr; Manage add-ons</strong> in Google Docs. Uninstalling removes its access immediately.
  Because SortDoc stores nothing, there is nothing left behind to delete.</p>

  <h2>Contact</h2>
  <p><a href="mailto:support@kapapi.dev">support@kapapi.dev</a></p>
"""

SORTDOC_TERMS = """
  <p class="eyebrow">SortDoc</p>
  <h1 style="font-size:clamp(2rem,5vw,2.8rem)">Terms of service</h1>
  <p style="color:var(--ink-muted)">Last updated: 1 September 2026</p>

  <h2>The agreement</h2>
  <p>These terms cover your use of SortDoc, a Google Docs editor add-on published by KaPaPi. By
  installing or using it you accept them. If you do not, do not install it.</p>

  <h2>What you get</h2>
  <p>SortDoc is provided free of charge. There is no trial, no paid tier and no payment of any kind.
  You may use it for personal or commercial work.</p>

  <h2>What it does to your documents</h2>
  <p>SortDoc reorders the paragraphs or list items you have selected. It refuses to act where it
  cannot act safely, but <strong>it does change your document</strong>, and that is the point of it.
  Google Docs keeps a full version history, and Ctrl+Z (Cmd+Z on Mac) undoes a sort. You remain
  responsible for your own documents and their backups.</p>

  <h2>No warranty</h2>
  <p>SortDoc is provided &ldquo;as is&rdquo;, without warranty of any kind, express or implied,
  including the warranties of merchantability, fitness for a particular purpose and
  non-infringement.</p>

  <h2>Limitation of liability</h2>
  <p>To the fullest extent permitted by law, the developer is not liable for any claim, damages or
  other liability &mdash; including loss of data, loss of profit, or consequential loss &mdash;
  arising from or in connection with SortDoc or its use. Nothing here limits any liability that
  cannot be limited under the law that applies to you.</p>

  <h2>Your data</h2>
  <p>SortDoc collects nothing, transmits nothing and stores nothing. See the
  <a href="/sortdoc/privacy.html">privacy policy</a>.</p>

  <h2>Source code and licence</h2>
  <p>SortDoc&rsquo;s source is public at
  <a href="https://github.com/kapapi-dev/sortdoc">github.com/kapapi-dev/sortdoc</a> under the MIT
  Licence. Those licence terms govern the source code; these terms govern the hosted add-on you
  install from the Google Workspace Marketplace.</p>

  <h2>Availability and changes</h2>
  <p>SortDoc may be changed, suspended or withdrawn at any time. Material changes to these terms
  will be published on this page with a new date above.</p>

  <h2>Governing law</h2>
  <p>These terms are governed by the laws of the Republic of Korea, without depriving you of the
  protection of any mandatory consumer law that applies where you live.</p>

  <h2>Contact</h2>
  <p><a href="mailto:support@kapapi.dev">support@kapapi.dev</a></p>
"""

SORTDOC_SUPPORT = """
  <p class="eyebrow">SortDoc</p>
  <h1 style="font-size:clamp(2rem,5vw,2.8rem)">Support</h1>
  <p class="lead">How to use it, what it refuses to do, and how to report a problem.</p>

  <h2>Getting started</h2>
  <ol>
    <li>Install SortDoc from the Google Workspace Marketplace.</li>
    <li>Open a Google Doc and select the paragraphs or list items you want in order.</li>
    <li>Choose <strong>Extensions &rarr; SortDoc &rarr; Sort A &rarr; Z</strong> or
        <strong>Sort Z &rarr; A</strong>.</li>
  </ol>
  <p>Press <strong>Ctrl+Z</strong> (<strong>Cmd+Z</strong> on Mac) to undo a sort. Google Docs also
  keeps a full version history under <strong>File &rarr; Version history</strong>.</p>

  <h2>Common questions</h2>

  <h3>It says my selection is not supported</h3>
  <p>SortDoc sorts a run of <em>consecutive</em> paragraphs or list items that sit next to each
  other in the same part of the document. A selection that skips over a table or an image, spans two
  different lists, or crosses two table cells is refused &mdash; reordering it would move things you
  did not select. Your document is not changed when this happens.</p>

  <h3>Numbers sorted in the wrong order</h3>
  <p>Numbers are compared as text, so <code>10</code> sorts before <code>9</code>. Natural numeric
  sorting is not implemented yet.</p>

  <h3>My extra spaces are still there</h3>
  <p>Deliberately. Leading and trailing whitespace is ignored when <em>comparing</em> lines, but
  never removed from the document &mdash; SortDoc only reorders, it does not rewrite. If you want
  that cleaned up, that is what <a href="/cleanpaste/">CleanPaste</a> is for.</p>

  <h3>The menu does not appear</h3>
  <p>Reload the document. Editor add-ons attach their menu when a document opens.</p>

  <h3>Can I use it on my phone or tablet?</h3>
  <p>No. Google Docs editor add-ons run in the desktop browser only.</p>

  <h2>Reporting a problem</h2>
  <ul>
    <li><strong>Open an issue:</strong>
        <a href="https://github.com/kapapi-dev/sortdoc/issues">github.com/kapapi-dev/sortdoc/issues</a></li>
    <li><strong>Email:</strong> <a href="mailto:support@kapapi.dev">support@kapapi.dev</a></li>
  </ul>
  <p>Please do not paste confidential document content into a public issue.</p>
"""

SENDARC_INDEX = """
  <p class="eyebrow" style="color:var(--sendarc)">A KaPaPi product for Windows</p>
  <h1 style="font-size:clamp(2.2rem,5.5vw,3.2rem)">SendArc</h1>
  <p class="lead">
    <strong>SendArc lets legacy Windows applications send email through Gmail without a
    desktop mail client.</strong> It bridges their Simple MAPI email command into a local
    preview, then sends only after you confirm the message.
  </p>

  <div class="note" style="border-left-color:var(--sendarc)">
    <p><strong>Release candidate:</strong> the public Windows beta is still completing its
    final real-account and installation checks. No downloadable release is being claimed yet.</p>
  </div>

  <h2>What stays familiar</h2>
  <p>Your existing accounting, ERP, CRM or other Windows application keeps using its normal
  email command. SendArc receives the message locally and shows the recipients, subject, body
  and attachments before anything is transmitted.</p>

  <h2>A deliberately narrow Google permission</h2>
  <table>
    <tr><th>Permission</th><th>What it allows</th></tr>
    <tr><td><code>gmail.send</code></td><td>Send the message you approve through Gmail</td></tr>
    <tr><td>Not requested</td><td>Reading your inbox, contacts, Drive files or account profile</td></tr>
  </table>
  <p>OAuth credentials are stored in Windows Credential Manager. Message content travels directly
  from the Windows app to Google after the explicit Send action; KaPaPi does not operate a relay
  that receives or stores the message.</p>
  <p>Read the <a href="/sendarc/privacy.html">SendArc privacy policy</a> for the complete data flow,
  retention rules and Google API Limited Use commitment.</p>

  <h2>Current beta scope</h2>
  <ul>
    <li>Windows 10 and Windows 11, with both 32-bit and 64-bit Simple MAPI applications.</li>
    <li>Gmail and Google Workspace accounts.</li>
    <li>Local preview with explicit Send, Cancel and retry behavior.</li>
    <li>Open-source implementation and an unsigned first beta while no paid signing route is used.</li>
  </ul>

  <p>
    <a class="button-link" href="https://sendarc.pages.dev/">Visit the SendArc product site &rarr;</a>
  </p>
  <p style="color:var(--ink-muted);font-size:0.95rem">
    Source and compatibility reports:
    <a href="https://github.com/KapapiDev/sendarc">github.com/KapapiDev/sendarc</a>
  </p>
"""

SENDARC_PRIVACY = """
  <p class="eyebrow" style="color:var(--sendarc)">SendArc</p>
  <h1 style="font-size:clamp(2rem,5vw,2.8rem)">Privacy policy</h1>
  <p style="color:var(--ink-muted)">Last updated: 2 September 2026</p>

  <div class="note" style="border-left-color:var(--sendarc)">
    <p>SendArc processes an outgoing email locally, shows it for review, and sends it directly
    from the Windows app to Google only after the user confirms Send. KaPaPi does not operate an
    email relay or read the user&rsquo;s inbox.</p>
  </div>

  <h2>Desktop application data</h2>
  <p>A Simple MAPI request may include To, Cc, Bcc, subject, body, formatting and attachments.
  SendArc writes the pending request and copied attachments to a per-user local queue so the user
  can review, send or discard it. Pending data remains on that Windows device until it is sent,
  discarded or removed through local maintenance.</p>
  <p>When the user confirms Send, SendArc builds the MIME message locally and sends it directly to
  Google&rsquo;s Gmail API over HTTPS. Message content is not sent through a KaPaPi or SendArc
  server.</p>

  <h2>Google account access</h2>
  <p>SendArc requests only <code>https://www.googleapis.com/auth/gmail.send</code>, which allows it
  to send the message the user approved. It does not request inbox-reading, mailbox-search,
  contacts, calendar, <code>gmail.compose</code>, <code>gmail.modify</code> or
  <code>mail.google.com</code> access.</p>
  <p>OAuth tokens are stored in Windows Credential Manager. They are not stored in local queue
  files, website analytics or KaPaPi servers. The user can disconnect SendArc and revoke access
  from their Google Account.</p>

  <h2>Google API Limited Use</h2>
  <p>SendArc&rsquo;s use and transfer of information received from Google APIs adheres to the
  <a href="https://developers.google.com/terms/api-services-user-data-policy">Google API Services
  User Data Policy</a>, including its Limited Use requirements. Google API data is used only to
  provide the prominent user-facing Gmail send feature, is not sold, is not used for advertising,
  and is not used to train generalized AI or machine-learning models.</p>

  <h2>Logs and app telemetry</h2>
  <p>The desktop beta has no hidden telemetry. Local diagnostics are designed to exclude OAuth
  tokens, recipients, subjects, bodies, attachment names and paths, Gmail message IDs and Gmail
  response bodies. Users should still inspect and sanitize diagnostics before sharing them.</p>

  <h2>Website and Business Beta data</h2>
  <p>The full product site at <a href="https://sendarc.pages.dev/">sendarc.pages.dev</a> is hosted
  by Cloudflare. Its optional Business Beta form stores work email, company, approximate seat
  range, current workflow, an optional note and basic campaign labels in Cloudflare D1. Do not
  submit message content, recipients, credentials or confidential attachments.</p>
  <p>Lead data is used only to evaluate and contact beta participants and is retained for no more
  than 12 months after the last product or beta contact. A one-way anti-abuse hash may be retained
  for no more than 24 hours. The site may record allowlisted page and CTA events without
  advertising cookies, cross-site identifiers or desktop email data.</p>

  <h2>Processors and disclosure</h2>
  <ul>
    <li>Google processes OAuth and Gmail API data under Google&rsquo;s policies.</li>
    <li>Cloudflare processes full-site delivery, security, Pages Functions and D1 data.</li>
    <li>GitHub hosts the source, releases and public issue forms and serves this KaPaPi page.</li>
  </ul>
  <p>KaPaPi does not sell personal data. Data may be disclosed only when required by law or to the
  processors above as necessary to operate the stated service.</p>

  <h2>Access and deletion</h2>
  <p>To request access to or deletion of a Business Beta record, email
  <a href="mailto:maxtop9843@gmail.com">maxtop9843@gmail.com</a> from the submitted address.
  SendArc is operated by 장형진 under the KaPaPi developer brand.</p>
"""

SENDARC_TERMS = """
  <p class="eyebrow" style="color:var(--sendarc)">SendArc</p>
  <h1 style="font-size:clamp(2rem,5vw,2.8rem)">Beta terms</h1>
  <p style="color:var(--ink-muted)">Last updated: 2 September 2026</p>

  <h2>The agreement</h2>
  <p>These terms cover evaluation of SendArc, a Windows utility published under the KaPaPi
  developer brand and operated by 장형진. By installing or using SendArc you accept them. If you
  do not accept them, do not install or use the beta.</p>

  <h2>Beta software</h2>
  <p>SendArc is pre-release software provided for evaluation without warranty. Test it with
  non-critical workflows first, keep appropriate backups, and review every local preview before
  sending. Compatibility depends on how each Windows application implements Simple MAPI.</p>

  <h2>Acceptable use</h2>
  <p>Use SendArc only with accounts, recipients and applications you are authorized to operate.
  Do not use it for unsolicited bulk mail, credential theft, bypassing access controls, unlawful
  content or infringement of another person&rsquo;s rights.</p>

  <h2>No payment today</h2>
  <p>The current Business Beta form is an expression of interest, not an order. No payment is
  collected. Any future paid offer will require separate, explicit terms.</p>

  <h2>Your data</h2>
  <p>The <a href="/sendarc/privacy.html">SendArc privacy policy</a> explains local message
  handling, direct Gmail API transmission, OAuth token storage and website data.</p>

  <h2>Open-source licences</h2>
  <p>Software rights are governed by the repository&rsquo;s licences and third-party notices.
  SendArc incorporates and modifies code from go-mapi under LGPL-3.0-or-later. These site terms do
  not reduce rights granted by that licence, and neither the go-mapi author nor Affixa endorses or
  is affiliated with SendArc.</p>

  <h2>No warranty and limitation</h2>
  <p>To the fullest extent permitted by law, the beta is provided &ldquo;as is&rdquo; without
  warranties, and the operator is not liable for indirect, incidental or consequential loss.
  Nothing here limits liability that cannot legally be limited or mandatory consumer rights.</p>

  <h2>Changes and governing law</h2>
  <p>Material changes will be published here with a new date. These terms are governed by the laws
  of the Republic of Korea without depriving users of mandatory protections that apply where they
  live.</p>

  <h2>Contact</h2>
  <p><a href="mailto:maxtop9843@gmail.com">maxtop9843@gmail.com</a></p>
"""

SENDARC_SUPPORT = """
  <p class="eyebrow" style="color:var(--sendarc)">SendArc</p>
  <h1 style="font-size:clamp(2rem,5vw,2.8rem)">Support</h1>
  <p class="lead">Get help without exposing private email, account or customer data.</p>

  <h2>Before reporting a problem</h2>
  <p>Record the SendArc version, Windows version, source application and whether it is 32-bit or
  64-bit if known. Describe the steps and visible result without including the real message.</p>

  <h2>Support channels</h2>
  <ul>
    <li><strong>Bug report:</strong>
      <a href="https://github.com/KapapiDev/sendarc/issues/new?template=bug_report.yml">open the
      sanitized bug form</a></li>
    <li><strong>Compatibility report:</strong>
      <a href="https://github.com/KapapiDev/sendarc/issues/new?template=compatibility_report.yml">report
      a Simple MAPI application</a></li>
    <li><strong>Feature request:</strong>
      <a href="https://github.com/KapapiDev/sendarc/issues/new?template=feature_request.yml">describe
      the user problem</a></li>
    <li><strong>Private contact or deletion request:</strong>
      <a href="mailto:maxtop9843@gmail.com">maxtop9843@gmail.com</a></li>
  </ul>

  <h2>Never include</h2>
  <p>Email bodies, recipient addresses, attachments, OAuth tokens, Google passwords, OAuth client
  credentials, private logs or confidential customer data. Sanitize diagnostics before sharing
  them.</p>
"""

PAGES = [
    ("cleanpaste", "terms.html",
     "CleanPaste terms of service | KaPaPi",
     "Terms of service for CleanPaste, a free Google Docs add-on that cleans up pasted text.",
     CLEANPASTE_TERMS),
    ("cleanpaste", "support.html",
     "CleanPaste support | KaPaPi",
     "Help for CleanPaste: how to use it, what it will not do, and how to report a problem.",
     CLEANPASTE_SUPPORT),
    ("sortdoc", "index.html",
     "SortDoc — Google Docs add-on that sorts selected paragraphs | KaPaPi",
     "SortDoc is a Google Docs add-on that sorts the paragraphs or list items you have selected, A-Z or Z-A, without losing their formatting.",
     SORTDOC_INDEX),
    ("sortdoc", "privacy.html",
     "SortDoc privacy policy | KaPaPi",
     "SortDoc collects nothing, transmits nothing and stores nothing. It can only see the Google Doc it is open in.",
     SORTDOC_PRIVACY),
    ("sortdoc", "terms.html",
     "SortDoc terms of service | KaPaPi",
     "Terms of service for SortDoc, a free Google Docs add-on that sorts selected paragraphs.",
     SORTDOC_TERMS),
    ("sortdoc", "support.html",
     "SortDoc support | KaPaPi",
     "Help for SortDoc: how to use it, what it refuses to do, and how to report a problem.",
     SORTDOC_SUPPORT),
    ("sendarc", "index.html",
     "SendArc — legacy Windows email through Gmail | KaPaPi",
     "SendArc bridges Simple MAPI email from legacy Windows applications to Gmail with a local preview and explicit send confirmation.",
     SENDARC_INDEX),
    ("sendarc", "privacy.html",
     "SendArc privacy policy | KaPaPi",
     "How SendArc processes local email previews, Gmail OAuth data and Business Beta records.",
     SENDARC_PRIVACY),
    ("sendarc", "terms.html",
     "SendArc beta terms | KaPaPi",
     "Plain-language terms for evaluating the SendArc Windows beta.",
     SENDARC_TERMS),
    ("sendarc", "support.html",
     "SendArc support | KaPaPi",
     "Support and sanitized issue-reporting routes for the SendArc Windows beta.",
     SENDARC_SUPPORT),
]
