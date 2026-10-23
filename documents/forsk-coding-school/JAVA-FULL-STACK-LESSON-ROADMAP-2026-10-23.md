# Java Full Stack lesson publication roadmap
Date: 23 October 2026
Brand: Forsk Coding School
Implementation repository: satnamkhowal/forsk-coding-school
Implementation PR: https://github.com/satnamkhowal/forsk-coding-school/pull/43
Implementation commit: 3667a13b0853b868bacd5a6b8ddb08396831771a
Owner: Forsk course-content workstream / central controller
Status: PLANNED original content; routed reference links implemented and locally verified.
Priority: P1 foundations/database/framework/API; P2 advanced/project/career deepening.

## Publication contract

The owner requested removing lock icons and connecting every curriculum topic to a descriptive tutorial URL, with unfinished lessons logged centrally for future writing.

The 40 original Forsk lessons below are not written or indexed yet. Their URLs are reserved by a local route and temporarily open a related primary-source/reference guide (HTTP 302, X-Robots-Tag: noindex, follow, Cache-Control: no-store). The course explains this reference-guide behavior. Unknown slugs return 404. Do not mark these rows COMPLETE merely because the redirects work.

Use each exact reserved URL when the original lesson is published. Physical lesson files/directories take precedence over the fallback rewrite. Preserve or redirect any substantive legacy tutorial rather than publishing duplicate competing pages.

Each lesson must include original explanations, prerequisites, a runnable example, exercise and expected output, common mistakes, version notes, authoritative further reading, course/module breadcrumb, previous/next links and a self canonical. Review modern JDK compatibility: Oracle's legacy tutorial references are not the course version specification. Add indexing/sitemap entry only after meaningful content and QA. Never publish thin indexable coming-soon placeholders.

## Topic queue

| Module | Topic | Reserved canonical URL | Original content status | Temporary reference |
| --- | --- | --- | --- | --- |
| 01 | Syntax and program structure | [/tutorials/java-full-stack/java-syntax-program-structure/](https://forskcodingschool.com/tutorials/java-full-stack/java-syntax-program-structure/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/) |
| 01 | Variables, data types and operators | [/tutorials/java-full-stack/java-variables-data-types-operators/](https://forskcodingschool.com/tutorials/java-full-stack/java-variables-data-types-operators/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html) |
| 01 | Control flow and problem solving | [/tutorials/java-full-stack/java-control-flow-problem-solving/](https://forskcodingschool.com/tutorials/java-full-stack/java-control-flow-problem-solving/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/flow.html) |
| 01 | Development environment | [/tutorials/java-full-stack/java-jdk-ide-setup/](https://forskcodingschool.com/tutorials/java-full-stack/java-jdk-ide-setup/) | PLANNED | [Reference](https://dev.java/learn/getting-started/) |
| 02 | Classes and objects | [/tutorials/java-full-stack/java-classes-objects/](https://forskcodingschool.com/tutorials/java-full-stack/java-classes-objects/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/java/javaOO/) |
| 02 | Inheritance and polymorphism | [/tutorials/java-full-stack/java-inheritance-polymorphism/](https://forskcodingschool.com/tutorials/java-full-stack/java-inheritance-polymorphism/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html) |
| 02 | Abstraction and interfaces | [/tutorials/java-full-stack/java-abstraction-interfaces/](https://forskcodingschool.com/tutorials/java-full-stack/java-abstraction-interfaces/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html) |
| 02 | Encapsulation and design principles | [/tutorials/java-full-stack/java-encapsulation-design-principles/](https://forskcodingschool.com/tutorials/java-full-stack/java-encapsulation-design-principles/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html) |
| 03 | List, Set and Map | [/tutorials/java-full-stack/java-list-set-map/](https://forskcodingschool.com/tutorials/java-full-stack/java-list-set-map/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/collections/interfaces/) |
| 03 | Iterators and collection patterns | [/tutorials/java-full-stack/java-iterators-collection-patterns/](https://forskcodingschool.com/tutorials/java-full-stack/java-iterators-collection-patterns/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/collections/interfaces/collection.html) |
| 03 | Generics | [/tutorials/java-full-stack/java-generics/](https://forskcodingschool.com/tutorials/java-full-stack/java-generics/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/java/generics/) |
| 03 | Comparable and Comparator | [/tutorials/java-full-stack/java-comparable-comparator/](https://forskcodingschool.com/tutorials/java-full-stack/java-comparable-comparator/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/collections/interfaces/order.html) |
| 04 | Exception handling | [/tutorials/java-full-stack/java-exception-handling/](https://forskcodingschool.com/tutorials/java-full-stack/java-exception-handling/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/essential/exceptions/) |
| 04 | File and stream I/O | [/tutorials/java-full-stack/java-file-stream-io/](https://forskcodingschool.com/tutorials/java-full-stack/java-file-stream-io/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/essential/io/streams.html) |
| 04 | Serialization concepts | [/tutorials/java-full-stack/java-serialization/](https://forskcodingschool.com/tutorials/java-full-stack/java-serialization/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/essential/io/objectstreams.html) |
| 04 | Logging and debugging | [/tutorials/java-full-stack/java-logging-debugging/](https://forskcodingschool.com/tutorials/java-full-stack/java-logging-debugging/) | PLANNED | [Reference](https://docs.oracle.com/en/java/javase/21/docs/api/java.logging/java/util/logging/package-summary.html) |
| 05 | SQL fundamentals | [/tutorials/java-full-stack/sql-fundamentals-java-developers/](https://forskcodingschool.com/tutorials/java-full-stack/sql-fundamentals-java-developers/) | PLANNED | [Reference](https://www.postgresql.org/docs/current/tutorial-sql.html) |
| 05 | JDBC connectivity | [/tutorials/java-full-stack/java-jdbc-connectivity/](https://forskcodingschool.com/tutorials/java-full-stack/java-jdbc-connectivity/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/jdbc/basics/connecting.html) |
| 05 | CRUD and transactions | [/tutorials/java-full-stack/jdbc-crud-transactions/](https://forskcodingschool.com/tutorials/java-full-stack/jdbc-crud-transactions/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/jdbc/basics/transactions.html) |
| 05 | Prepared statements | [/tutorials/java-full-stack/jdbc-prepared-statements/](https://forskcodingschool.com/tutorials/java-full-stack/jdbc-prepared-statements/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/jdbc/basics/prepared.html) |
| 06 | Dependency injection | [/tutorials/java-full-stack/spring-dependency-injection/](https://forskcodingschool.com/tutorials/java-full-stack/spring-dependency-injection/) | PLANNED | [Reference](https://docs.spring.io/spring-framework/reference/core/beans.html) |
| 06 | Configuration and environments | [/tutorials/java-full-stack/spring-configuration-profiles/](https://forskcodingschool.com/tutorials/java-full-stack/spring-configuration-profiles/) | PLANNED | [Reference](https://docs.spring.io/spring-boot/reference/features/profiles.html) |
| 06 | MVC and layered architecture | [/tutorials/java-full-stack/spring-mvc-layered-architecture/](https://forskcodingschool.com/tutorials/java-full-stack/spring-mvc-layered-architecture/) | PLANNED | [Reference](https://docs.spring.io/spring-framework/reference/web/webmvc.html) |
| 06 | Validation and error handling | [/tutorials/java-full-stack/spring-validation-error-handling/](https://forskcodingschool.com/tutorials/java-full-stack/spring-validation-error-handling/) | PLANNED | [Reference](https://spring.io/guides/gs/validating-form-input/) |
| 07 | REST API fundamentals | [/tutorials/java-full-stack/java-rest-api-fundamentals/](https://forskcodingschool.com/tutorials/java-full-stack/java-rest-api-fundamentals/) | PLANNED | [Reference](https://spring.io/guides/gs/rest-service/) |
| 07 | JSON and HTTP | [/tutorials/java-full-stack/json-http-java/](https://forskcodingschool.com/tutorials/java-full-stack/json-http-java/) | PLANNED | [Reference](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/Overview) |
| 07 | API documentation and testing | [/tutorials/java-full-stack/spring-rest-api-documentation-testing/](https://forskcodingschool.com/tutorials/java-full-stack/spring-rest-api-documentation-testing/) | PLANNED | [Reference](https://spring.io/guides/gs/testing-web/) |
| 07 | Service integration | [/tutorials/java-full-stack/java-service-integration/](https://forskcodingschool.com/tutorials/java-full-stack/java-service-integration/) | PLANNED | [Reference](https://spring.io/guides/gs/consuming-rest/) |
| 08 | Concurrency and multithreading | [/tutorials/java-full-stack/java-concurrency-multithreading/](https://forskcodingschool.com/tutorials/java-full-stack/java-concurrency-multithreading/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/essential/concurrency/) |
| 08 | Design patterns and clean code | [/tutorials/java-full-stack/java-design-patterns-clean-code/](https://forskcodingschool.com/tutorials/java-full-stack/java-design-patterns-clean-code/) | PLANNED | [Reference](https://docs.oracle.com/javase/tutorial/java/concepts/) |
| 08 | Performance and memory | [/tutorials/java-full-stack/java-performance-memory/](https://forskcodingschool.com/tutorials/java-full-stack/java-performance-memory/) | PLANNED | [Reference](https://docs.oracle.com/en/java/javase/21/gctuning/) |
| 08 | Secure application practices | [/tutorials/java-full-stack/java-application-security/](https://forskcodingschool.com/tutorials/java-full-stack/java-application-security/) | PLANNED | [Reference](https://docs.spring.io/spring-security/reference/) |
| 09 | Architecture planning | [/tutorials/java-full-stack/java-project-architecture-planning/](https://forskcodingschool.com/tutorials/java-full-stack/java-project-architecture-planning/) | PLANNED | [Reference](https://spring.io/guides/tutorials/rest/) |
| 09 | Database-backed project | [/tutorials/java-full-stack/java-database-project/](https://forskcodingschool.com/tutorials/java-full-stack/java-database-project/) | PLANNED | [Reference](https://spring.io/guides/gs/accessing-data-jpa/) |
| 09 | Testing and debugging | [/tutorials/java-full-stack/java-testing-debugging/](https://forskcodingschool.com/tutorials/java-full-stack/java-testing-debugging/) | PLANNED | [Reference](https://spring.io/guides/gs/testing-web/) |
| 09 | Packaging and deployment | [/tutorials/java-full-stack/spring-boot-packaging-deployment/](https://forskcodingschool.com/tutorials/java-full-stack/spring-boot-packaging-deployment/) | PLANNED | [Reference](https://spring.io/guides/gs/spring-boot/) |
| 10 | Git and collaboration | [/tutorials/java-full-stack/git-collaboration-java-projects/](https://forskcodingschool.com/tutorials/java-full-stack/git-collaboration-java-projects/) | PLANNED | [Reference](https://git-scm.com/book/en/v2) |
| 10 | Resume and portfolio | [/tutorials/java-full-stack/java-developer-resume-portfolio/](https://forskcodingschool.com/tutorials/java-full-stack/java-developer-resume-portfolio/) | PLANNED | [Reference](https://forskcodingschool.com/blog/java-project-ideas-for-final-year-students/) |
| 10 | Technical interview preparation | [/tutorials/java-full-stack/java-technical-interview-preparation/](https://forskcodingschool.com/tutorials/java-full-stack/java-technical-interview-preparation/) | PLANNED | [Reference](https://forskcodingschool.com/java-interview-preparation-jaipur) |
| 10 | Career roadmap | [/tutorials/java-full-stack/java-developer-career-roadmap/](https://forskcodingschool.com/tutorials/java-full-stack/java-developer-career-roadmap/) | PLANNED | [Reference](https://forskcodingschool.com/blog/why-java-is-still-important-for-software-developers/) |

## Additional course-content audit work

- P1: Expand approved Java Full Stack curriculum coverage for HTML, CSS, JavaScript, the frontend framework, frontend/backend integration and a full-stack capstone; current 40-topic outline is predominantly Java/backend and generic professional workflow.
- P1: Replace generic Skills/Tools labels with verified technologies and actual project outputs.
- P1: Establish approved course-to-faculty mappings for other courses; the compact layout supports multiple assigned faculty without inventing a fourth Java instructor.
- P2: Consolidate duplicate overview/highlights/audience wording.
- P2: Evaluate shorter enquiry entry/progressive fields with the lead-routing owner; do not silently break required backend fields.
- P2: Inventory introduced-course and bespoke templates before claiming every catalogue page has migrated.

## Evidence and next action

Five actual PHP templates passed strict full rendering and syntax checks locally. Java had 40 topic anchors, no locks, one enquiry form, three assigned faculty, valid JSON-LD and one brochure widget. Responsive checks covered 320/390/768/1440px. All 40 route redirects passed on local Apache 2.4. Existing Java project/interview/career reference pages were opened and their headings checked. Existing Java brochure downloaded: 1,565,324 bytes. No live lead submitted.

Detailed audit: https://github.com/satnamkhowal/forsk-coding-school/blob/feature/course-structure-qa-20261023/docs/course-structure-audit-2026-10-23.md
PR checks: https://github.com/satnamkhowal/forsk-coding-school/actions/runs/39953935843

Next content action: write and QA the first four foundation lessons at their reserved URLs, replace temporary reference routing for those lessons and record the publication evidence. This is a backlog, not a scheduled automation.


## Repository checkpoint

PR #43 merged; source merge SHA `0d14949fad7bb48a896e82f74b6ca7b1249d1339`. Course structure QA run `39953935843` completed SUCCESS. Public Java course checked after merge: old layout markers still present; host deployment is pending. Original lesson content remains PLANNED.
