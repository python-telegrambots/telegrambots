from dataclasses import dataclass, field
from typing import Optional

from ..._client_utilities import ClientTargetable
from ..api_object import TelegramBotsObject

from .voice import Voice
from .video_chat_ended import VideoChatEnded
from .proximity_alert_triggered import ProximityAlertTriggered
from .inline_keyboard_markup import InlineKeyboardMarkup
from .contact import Contact
from .invoice import Invoice
from .photo_size import PhotoSize
from .game import Game
from .document import Document
from .user import User
from .web_app_data import WebAppData
from .video_chat_started import VideoChatStarted
from .sticker import Sticker
from .dice import Dice
from .video import Video
from .video_note import VideoNote
from .video_chat_participants_invited import VideoChatParticipantsInvited
from .chat import Chat
from .poll import Poll
from .video_chat_scheduled import VideoChatScheduled
from .message_entity import MessageEntity
from .passport_data import PassportData
from .message_auto_delete_timer_changed import MessageAutoDeleteTimerChanged
from .audio import Audio
from .animation import Animation
from .location import Location
from .venue import Venue
from .successful_payment import SuccessfulPayment


@dataclass(init=True, repr=True, slots=True)
class Message(TelegramBotsObject, ClientTargetable):
    # --- description here ---
    """This object represents a message.

    More info at: https://core.telegram.org/bots/api/#message
    """

    # --- properties here ---
    message_id: int = field(metadata={"ac_type": [int], "ac_name": "message_id"})
    """Unique message identifier inside this chat
    """

    date: int = field(metadata={"ac_type": [int], "ac_name": "date"})
    """Date the message was sent in Unix time
    """

    chat: Chat = field(metadata={"ac_type": [Chat], "ac_name": "chat"})
    """Conversation the message belongs to
    """

    from_user: Optional[User] = field(
        default=None, metadata={"ac_type": [User], "ac_name": "from"}
    )
    """*Optional*. Sender of the message; empty for messages sent to channels. For backward compatibility, the field contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
    """

    sender_chat: Optional[Chat] = field(
        default=None, metadata={"ac_type": [Chat], "ac_name": "sender_chat"}
    )
    """*Optional*. Sender of the message, sent on behalf of a chat. For example, the channel itself for channel posts, the supergroup itself for messages from anonymous group administrators, the linked channel for messages automatically forwarded to the discussion group. For backward compatibility, the field *from* contains a fake sender user in non-channel chats, if the message was sent on behalf of a chat.
    """

    forward_from: Optional[User] = field(
        default=None, metadata={"ac_type": [User], "ac_name": "forward_from"}
    )
    """*Optional*. For forwarded messages, sender of the original message
    """

    forward_from_chat: Optional[Chat] = field(
        default=None, metadata={"ac_type": [Chat], "ac_name": "forward_from_chat"}
    )
    """*Optional*. For messages forwarded from channels or from anonymous administrators, information about the original sender chat
    """

    forward_from_message_id: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "forward_from_message_id"}
    )
    """*Optional*. For messages forwarded from channels, identifier of the original message in the channel
    """

    forward_signature: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "forward_signature"}
    )
    """*Optional*. For forwarded messages that were originally sent in channels or by an anonymous chat administrator, signature of the message sender if present
    """

    forward_sender_name: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "forward_sender_name"}
    )
    """*Optional*. Sender's name for messages forwarded from users who disallow adding a link to their account in forwarded messages
    """

    forward_date: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "forward_date"}
    )
    """*Optional*. For forwarded messages, date the original message was sent in Unix time
    """

    is_automatic_forward: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "is_automatic_forward"}
    )
    """*Optional*. True, if the message is a channel post that was automatically forwarded to the connected discussion group
    """

    reply_to_message: Optional["Message"] = field(
        default=None, metadata={"ac_type": ["Message"], "ac_name": "reply_to_message"}
    )
    """*Optional*. For replies, the original message. Note that the Message object in this field will not contain further *reply\\_to\\_message* fields even if it itself is a reply.
    """

    via_bot: Optional[User] = field(
        default=None, metadata={"ac_type": [User], "ac_name": "via_bot"}
    )
    """*Optional*. Bot through which the message was sent
    """

    edit_date: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "edit_date"}
    )
    """*Optional*. Date the message was last edited in Unix time
    """

    has_protected_content: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "has_protected_content"}
    )
    """*Optional*. True, if the message can't be forwarded
    """

    media_group_id: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "media_group_id"}
    )
    """*Optional*. The unique identifier of a media message group this message belongs to
    """

    author_signature: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "author_signature"}
    )
    """*Optional*. Signature of the post author for messages in channels, or the custom title of an anonymous group administrator
    """

    text: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "text"}
    )
    """*Optional*. For text messages, the actual UTF-8 text of the message, 0-4096 characters
    """

    entities: Optional[list[MessageEntity]] = field(
        default=None, metadata={"ac_type": [MessageEntity], "ac_name": "entities"}
    )
    """*Optional*. For text messages, special entities like usernames, URLs, bot commands, etc. that appear in the text
    """

    animation: Optional[Animation] = field(
        default=None, metadata={"ac_type": [Animation], "ac_name": "animation"}
    )
    """*Optional*. Message is an animation, information about the animation. For backward compatibility, when this field is set, the *document* field will also be set
    """

    audio: Optional[Audio] = field(
        default=None, metadata={"ac_type": [Audio], "ac_name": "audio"}
    )
    """*Optional*. Message is an audio file, information about the file
    """

    document: Optional[Document] = field(
        default=None, metadata={"ac_type": [Document], "ac_name": "document"}
    )
    """*Optional*. Message is a general file, information about the file
    """

    photo: Optional[list[PhotoSize]] = field(
        default=None, metadata={"ac_type": [PhotoSize], "ac_name": "photo"}
    )
    """*Optional*. Message is a photo, available sizes of the photo
    """

    sticker: Optional[Sticker] = field(
        default=None, metadata={"ac_type": [Sticker], "ac_name": "sticker"}
    )
    """*Optional*. Message is a sticker, information about the sticker
    """

    video: Optional[Video] = field(
        default=None, metadata={"ac_type": [Video], "ac_name": "video"}
    )
    """*Optional*. Message is a video, information about the video
    """

    video_note: Optional[VideoNote] = field(
        default=None, metadata={"ac_type": [VideoNote], "ac_name": "video_note"}
    )
    """*Optional*. Message is a [video note](https://telegram.org/blog/video-messages-and-telescope), information about the video message
    """

    voice: Optional[Voice] = field(
        default=None, metadata={"ac_type": [Voice], "ac_name": "voice"}
    )
    """*Optional*. Message is a voice message, information about the file
    """

    caption: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "caption"}
    )
    """*Optional*. Caption for the animation, audio, document, photo, video or voice, 0-1024 characters
    """

    caption_entities: Optional[list[MessageEntity]] = field(
        default=None,
        metadata={"ac_type": [MessageEntity], "ac_name": "caption_entities"},
    )
    """*Optional*. For messages with a caption, special entities like usernames, URLs, bot commands, etc. that appear in the caption
    """

    contact: Optional[Contact] = field(
        default=None, metadata={"ac_type": [Contact], "ac_name": "contact"}
    )
    """*Optional*. Message is a shared contact, information about the contact
    """

    dice: Optional[Dice] = field(
        default=None, metadata={"ac_type": [Dice], "ac_name": "dice"}
    )
    """*Optional*. Message is a dice with random value
    """

    game: Optional[Game] = field(
        default=None, metadata={"ac_type": [Game], "ac_name": "game"}
    )
    """*Optional*. Message is a game, information about the game. [More about games »](https://core.telegram.org/bots/api/#games)
    """

    poll: Optional[Poll] = field(
        default=None, metadata={"ac_type": [Poll], "ac_name": "poll"}
    )
    """*Optional*. Message is a native poll, information about the poll
    """

    venue: Optional[Venue] = field(
        default=None, metadata={"ac_type": [Venue], "ac_name": "venue"}
    )
    """*Optional*. Message is a venue, information about the venue. For backward compatibility, when this field is set, the *location* field will also be set
    """

    location: Optional[Location] = field(
        default=None, metadata={"ac_type": [Location], "ac_name": "location"}
    )
    """*Optional*. Message is a shared location, information about the location
    """

    new_chat_members: Optional[list[User]] = field(
        default=None, metadata={"ac_type": [User], "ac_name": "new_chat_members"}
    )
    """*Optional*. New members that were added to the group or supergroup and information about them (the bot itself may be one of these members)
    """

    left_chat_member: Optional[User] = field(
        default=None, metadata={"ac_type": [User], "ac_name": "left_chat_member"}
    )
    """*Optional*. A member was removed from the group, information about them (this member may be the bot itself)
    """

    new_chat_title: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "new_chat_title"}
    )
    """*Optional*. A chat title was changed to this value
    """

    new_chat_photo: Optional[list[PhotoSize]] = field(
        default=None, metadata={"ac_type": [PhotoSize], "ac_name": "new_chat_photo"}
    )
    """*Optional*. A chat photo was change to this value
    """

    delete_chat_photo: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "delete_chat_photo"}
    )
    """*Optional*. Service message: the chat photo was deleted
    """

    group_chat_created: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "group_chat_created"}
    )
    """*Optional*. Service message: the group has been created
    """

    supergroup_chat_created: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "supergroup_chat_created"}
    )
    """*Optional*. Service message: the supergroup has been created. This field can't be received in a message coming through updates, because bot can't be a member of a supergroup when it is created. It can only be found in reply\\_to\\_message if someone replies to a very first message in a directly created supergroup.
    """

    channel_chat_created: Optional[bool] = field(
        default=None, metadata={"ac_type": [bool], "ac_name": "channel_chat_created"}
    )
    """*Optional*. Service message: the channel has been created. This field can't be received in a message coming through updates, because bot can't be a member of a channel when it is created. It can only be found in reply\\_to\\_message if someone replies to a very first message in a channel.
    """

    message_auto_delete_timer_changed: Optional[MessageAutoDeleteTimerChanged] = field(
        default=None,
        metadata={
            "ac_type": [MessageAutoDeleteTimerChanged],
            "ac_name": "message_auto_delete_timer_changed",
        },
    )
    """*Optional*. Service message: auto-delete timer settings changed in the chat
    """

    migrate_to_chat_id: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "migrate_to_chat_id"}
    )
    """*Optional*. The group has been migrated to a supergroup with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    """

    migrate_from_chat_id: Optional[int] = field(
        default=None, metadata={"ac_type": [int], "ac_name": "migrate_from_chat_id"}
    )
    """*Optional*. The supergroup has been migrated from a group with the specified identifier. This number may have more than 32 significant bits and some programming languages may have difficulty/silent defects in interpreting it. But it has at most 52 significant bits, so a signed 64-bit integer or double-precision float type are safe for storing this identifier.
    """

    pinned_message: Optional["Message"] = field(
        default=None, metadata={"ac_type": ["Message"], "ac_name": "pinned_message"}
    )
    """*Optional*. Specified message was pinned. Note that the Message object in this field will not contain further *reply\\_to\\_message* fields even if it is itself a reply.
    """

    invoice: Optional[Invoice] = field(
        default=None, metadata={"ac_type": [Invoice], "ac_name": "invoice"}
    )
    """*Optional*. Message is an invoice for a [payment](https://core.telegram.org/bots/api/#payments), information about the invoice. [More about payments »](https://core.telegram.org/bots/api/#payments)
    """

    successful_payment: Optional[SuccessfulPayment] = field(
        default=None,
        metadata={"ac_type": [SuccessfulPayment], "ac_name": "successful_payment"},
    )
    """*Optional*. Message is a service message about a successful payment, information about the payment. [More about payments »](https://core.telegram.org/bots/api/#payments)
    """

    connected_website: Optional[str] = field(
        default=None, metadata={"ac_type": [str], "ac_name": "connected_website"}
    )
    """*Optional*. The domain name of the website on which the user has logged in. [More about Telegram Login »](https://core.telegram.org/widgets/login)
    """

    passport_data: Optional[PassportData] = field(
        default=None, metadata={"ac_type": [PassportData], "ac_name": "passport_data"}
    )
    """*Optional*. Telegram Passport data
    """

    proximity_alert_triggered: Optional[ProximityAlertTriggered] = field(
        default=None,
        metadata={
            "ac_type": [ProximityAlertTriggered],
            "ac_name": "proximity_alert_triggered",
        },
    )
    """*Optional*. Service message. A user in the chat triggered another user's proximity alert while sharing Live Location.
    """

    video_chat_scheduled: Optional[VideoChatScheduled] = field(
        default=None,
        metadata={"ac_type": [VideoChatScheduled], "ac_name": "video_chat_scheduled"},
    )
    """*Optional*. Service message: video chat scheduled
    """

    video_chat_started: Optional[VideoChatStarted] = field(
        default=None,
        metadata={"ac_type": [VideoChatStarted], "ac_name": "video_chat_started"},
    )
    """*Optional*. Service message: video chat started
    """

    video_chat_ended: Optional[VideoChatEnded] = field(
        default=None,
        metadata={"ac_type": [VideoChatEnded], "ac_name": "video_chat_ended"},
    )
    """*Optional*. Service message: video chat ended
    """

    video_chat_participants_invited: Optional[VideoChatParticipantsInvited] = field(
        default=None,
        metadata={
            "ac_type": [VideoChatParticipantsInvited],
            "ac_name": "video_chat_participants_invited",
        },
    )
    """*Optional*. Service message: new participants invited to a video chat
    """

    web_app_data: Optional[WebAppData] = field(
        default=None, metadata={"ac_type": [WebAppData], "ac_name": "web_app_data"}
    )
    """*Optional*. Service message: data sent by a Web App
    """

    reply_markup: Optional[InlineKeyboardMarkup] = field(
        default=None,
        metadata={"ac_type": [InlineKeyboardMarkup], "ac_name": "reply_markup"},
    )
    """*Optional*. Inline keyboard attached to the message. `login_url` buttons are represented as ordinary `url` buttons.
    """
