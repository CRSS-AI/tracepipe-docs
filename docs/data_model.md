# Data Model

_Last reviewed: 2026-02-20_

## Lineage

This data model is derived from the [AutoActivity data model](https://github.com/CRSS-AI/autoactivity-docs/blob/main/docs/backend/data_model.md). The Suite, Action, Tool, and mapping entities are preserved intact. The Activity Execution layer has been simplified: Sessions represent raw trace uploads and Examples represent processed training data. The Task/Activity/Case/Instance orchestration hierarchy has been removed.

## Scope

Capture the authoritative abstractions and entities that underpin trace ingestion, suite/action/tool mapping, and training data generation.

## Modeling Principles

- **Single source of truth**: Every persistent entity has a single owning service with explicit boundaries.
- **Versioned schemas**: Breaking changes require a version bump and migration plan.
- **Typed identifiers**: Use UUID namespaces to avoid cross-entity collisions.
- **Conventional formats**: Use JSONL for serialized training examples.

## Entity Catalog

```mermaid
---
config:
  layout: elk
  nodePlacementStrategy: LINEAR_SEGMENTS
---

classDiagram
    class Suite {
        +uuid id
        +string name
        +List~Action~ actions
        +List~ActionToolMap~ actionToolMaps
    }
    class Action {
        +uuid id
        +uuid suiteId
        +Suite suite
        +string name
        +List~ActionParameter~ parameters
    }
    class ActionParameter {
        +uuid id
        +uuid actionId
        +Action action
        +string name
        +ParameterType type
        +bool required
    }
    class McpServer {
        +uuid id
        +string name
        +List~Tool~ tools
    }
    class Tool {
        +uuid id
        +uuid mcpServerId
        +McpServer mcpServer
        +string name
        +List~ToolParameter~ parameters
    }
    class ToolParameter {
        +uuid id
        +uuid toolId
        +Tool tool
        +string name
        +ParameterType type
        +bool required
    }
    class ActionToolMap {
        +uuid id
        +uuid suiteId
        +Suite suite
        +uuid mcpServerId
        +McpServer mcpServer
        +List~ActionToolMapping~ toolMappings
    }
    class ActionToolMapping {
        +uuid id
        +uuid actionToolMapId
        +ActionToolMap actionToolMap
        +uuid actionId
        +Action action
        +uuid toolId
        +Tool tool
        +List~ActionToolParameterMapping~ parameterMappings
    }
    class ActionToolParameterMapping {
        +uuid id
        +uuid actionToolMappingId
        +ActionToolMapping actionToolMapping
        +uuid actionParameterId
        +ActionParameter actionParameter
        +uuid toolParameterId
        +ToolParameter toolParameter
    }
    class Model {
        +uuid id
        +Provider provider
        +string name
    }
    class User {
        +uuid id
        +string displayName
    }
    class Session {
        +uuid id
        +uuid userId
        +User user
        +uuid suiteId
        +Suite suite
        +text description
        +timestamp createdAt
        +string storagePath
    }
    class Example {
        +uuid id
        +uuid sessionId
        +Session session
        +uuid modelId
        +Model model
        +uuid actionToolMapId
        +ActionToolMap actionToolMap
        +json modelConfiguration
        +string storagePath
        +ExampleStatus status
        +timestamp createdAt
    }

    Suite *-- Action
    Action *-- ActionParameter
    McpServer *-- Tool
    Tool *-- ToolParameter
    ActionToolMap --> Suite
    ActionToolMap --> McpServer
    ActionToolMap *-- ActionToolMapping
    ActionToolMapping --> Action
    ActionToolMapping --> Tool
    ActionToolMapping *-- ActionToolParameterMapping
    ActionToolParameterMapping --> ActionParameter
    ActionToolParameterMapping --> ToolParameter
    Session --> User
    Session --> Suite
    Example --> Session
    Example --> Model
    Example --> ActionToolMap
```

### Suite, Action, and Tool entities

```mermaid
---
config:
  layout: elk
  nodePlacementStrategy: LINEAR_SEGMENTS
---

classDiagram
    class Suite {
        +uuid id
        +string name
        +List~Action~ actions
        +List~ActionToolMap~ actionToolMaps
    }
    class Action {
        +uuid id
        +uuid suiteId
        +Suite suite
        +string name
        +List~ActionParameter~ parameters
    }
    class ActionParameter {
        +uuid id
        +uuid actionId
        +Action action
        +string name
        +ParameterType type
        +bool required
    }
    class McpServer {
        +uuid id
        +string name
        +List~Tool~ tools
    }
    class Tool {
        +uuid id
        +uuid mcpServerId
        +McpServer mcpServer
        +string name
        +List~ToolParameter~ parameters
    }
    class ToolParameter {
        +uuid id
        +uuid toolId
        +Tool tool
        +string name
        +ParameterType type
        +bool required
    }
    class ActionToolMap {
        +uuid id
        +uuid suiteId
        +Suite suite
        +uuid mcpServerId
        +McpServer mcpServer
        +List~ActionToolMapping~ toolMappings
    }
    class ActionToolMapping {
        +uuid id
        +uuid actionToolMapId
        +ActionToolMap actionToolMap
        +uuid actionId
        +Action action
        +uuid toolId
        +Tool tool
        +List~ActionToolParameterMapping~ parameterMappings
    }
    class ActionToolParameterMapping {
        +uuid id
        +uuid actionToolMappingId
        +ActionToolMapping actionToolMapping
        +uuid actionParameterId
        +ActionParameter actionParameter
        +uuid toolParameterId
        +ToolParameter toolParameter
    }

    Suite *-- Action
    Action *-- ActionParameter
    McpServer *-- Tool
    Tool *-- ToolParameter
    ActionToolMap --> Suite
    ActionToolMap --> McpServer
    ActionToolMap *-- ActionToolMapping
    ActionToolMapping --> Action
    ActionToolMapping --> Tool
    ActionToolMapping *-- ActionToolParameterMapping
    ActionToolParameterMapping --> ActionParameter
    ActionToolParameterMapping --> ToolParameter
```

### Session and Example Focus

```mermaid
---
config:
  layout: elk
  nodePlacementStrategy: LINEAR_SEGMENTS
---

classDiagram
    class User {
        +uuid id
        +string displayName
    }
    class Suite {
        +uuid id
        +string name
    }
    class Model {
        +uuid id
        +Provider provider
        +string name
    }
    class ActionToolMap {
        +uuid id
        +uuid suiteId
        +uuid mcpServerId
    }
    class Session {
        +uuid id
        +uuid userId
        +User user
        +uuid suiteId
        +Suite suite
        +text description
        +timestamp createdAt
        +string storagePath
    }
    class Example {
        +uuid id
        +uuid sessionId
        +Session session
        +uuid modelId
        +Model model
        +uuid actionToolMapId
        +ActionToolMap actionToolMap
        +json modelConfiguration
        +string storagePath
        +ExampleStatus status
        +timestamp createdAt
    }

    Session --> User
    Session --> Suite
    Example --> Session
    Example --> Model
    Example --> ActionToolMap
```

## Entity Guidance

### Suite, Action, and Tool entities

- **Suite**: Describes the human-facing application environment (e.g., Gmail). Maintains the set of canonical `Action` definitions and available `ActionToolMap` variants.
- **Action**: Canonical action definition scoped to a Suite. Parameters capture the inputs the action expects using shared parameter metadata.
- **ActionParameter**: Defines a single action input, including type metadata (`ParameterType`) and required flags.
- **McpServer**: Describes the agent-facing tool server. Owns the concrete catalog of `Tool` contracts.
- **Tool**: Operation invokable by an agent. Each Tool references its owning McpServer and exposes parameters with the same structure as actions.
- **ToolParameter**: Mirrors `ActionParameter` structure for MCP tool inputs.
- **ActionToolMap**: Binding between a Suite and its backing McpServer tool surface. `toolMappings` keep action-to-tool bindings auditable.
- **ActionToolMapping**: Associates an Action with the specific Tool surfaced in the same ActionToolMap, plus parameter bindings.
- **ActionToolParameterMapping**: Codifies how each ActionParameter maps onto a ToolParameter.

### Execution Entities

- **Model**: Logical representation of an LLM or policy artifact, scoped by `provider` (enum) and `name`. Configuration is stored per-Example rather than per-Model.
- **User**: Representation of the human operator uploading trace data.
- **Session**: Represents a trace upload from a user. Contains raw input event trace data at `storagePath`. Sessions are scoped to a Suite. The optional `description` field (TEXT) allows users to annotate what the trace captures.
- **Example**: Processed training data derived from a Session. Links to the Model and ActionToolMap used during processing. The `modelConfiguration` field captures provider-specific parameters (temperature, routing hints). The `storagePath` points to JSONL-serialized training messages. The `status` field (`ExampleStatus` enum: `PENDING`, `PROCESSING`, `COMPLETED`, `FAILED`) tracks processing progress. `createdAt` records when the example was generated.

## Storage Conventions

### Session Storage

Session traces are stored at `storagePath` with the following structure:

```
sessions/<session-id>/
└── input_events.jsonl      # User input trace (keyboard, mouse, touch)
```

### Example Storage

Examples are stored at `storagePath` as JSONL files containing training messages:

```
examples/<example-id>/
└── messages.jsonl          # Training conversation format
```

The JSONL format follows the conventional chat completion structure with `role` and `content` fields.
