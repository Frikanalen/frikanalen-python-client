import datetime
from http import HTTPStatus
from typing import Any, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.paginated_video_list import PaginatedVideoList
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    categories_name_icontains: Union[Unset, list[str]] = UNSET,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    creator_email: Union[Unset, str] = UNSET,
    duration: Union[Unset, str] = UNSET,
    duration_gt: Union[Unset, str] = UNSET,
    duration_gte: Union[Unset, str] = UNSET,
    duration_lt: Union[Unset, str] = UNSET,
    duration_lte: Union[Unset, str] = UNSET,
    framerate: Union[Unset, int] = UNSET,
    has_tono_records: Union[Unset, bool] = UNSET,
    is_filler: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    organization: Union[Unset, int] = UNSET,
    played_count_web: Union[Unset, int] = UNSET,
    played_count_web_gt: Union[Unset, int] = UNSET,
    played_count_web_gte: Union[Unset, int] = UNSET,
    played_count_web_lt: Union[Unset, int] = UNSET,
    played_count_web_lte: Union[Unset, int] = UNSET,
    publish_on_web: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    ref_url: Union[Unset, str] = UNSET,
    ref_url_icontains: Union[Unset, str] = UNSET,
    ref_url_startswith: Union[Unset, str] = UNSET,
    updated_time_after: Union[Unset, datetime.datetime] = UNSET,
    updated_time_before: Union[Unset, datetime.datetime] = UNSET,
    uploaded_time_after: Union[Unset, datetime.datetime] = UNSET,
    uploaded_time_before: Union[Unset, datetime.datetime] = UNSET,
) -> dict[str, Any]:
    params: dict[str, Any] = {}

    json_categories_name_icontains: Union[Unset, list[str]] = UNSET
    if not isinstance(categories_name_icontains, Unset):
        json_categories_name_icontains = categories_name_icontains

    params["categories__name__icontains"] = json_categories_name_icontains

    json_created_time_after: Union[Unset, str] = UNSET
    if not isinstance(created_time_after, Unset):
        json_created_time_after = created_time_after.isoformat()
    params["created_time_after"] = json_created_time_after

    json_created_time_before: Union[Unset, str] = UNSET
    if not isinstance(created_time_before, Unset):
        json_created_time_before = created_time_before.isoformat()
    params["created_time_before"] = json_created_time_before

    params["creator__email"] = creator_email

    params["duration"] = duration

    params["duration__gt"] = duration_gt

    params["duration__gte"] = duration_gte

    params["duration__lt"] = duration_lt

    params["duration__lte"] = duration_lte

    params["framerate"] = framerate

    params["has_tono_records"] = has_tono_records

    params["is_filler"] = is_filler

    params["limit"] = limit

    params["name"] = name

    params["name__icontains"] = name_icontains

    params["offset"] = offset

    params["ordering"] = ordering

    params["organization"] = organization

    params["played_count_web"] = played_count_web

    params["played_count_web__gt"] = played_count_web_gt

    params["played_count_web__gte"] = played_count_web_gte

    params["played_count_web__lt"] = played_count_web_lt

    params["played_count_web__lte"] = played_count_web_lte

    params["publish_on_web"] = publish_on_web

    params["q"] = q

    params["ref_url"] = ref_url

    params["ref_url__icontains"] = ref_url_icontains

    params["ref_url__startswith"] = ref_url_startswith

    json_updated_time_after: Union[Unset, str] = UNSET
    if not isinstance(updated_time_after, Unset):
        json_updated_time_after = updated_time_after.isoformat()
    params["updated_time_after"] = json_updated_time_after

    json_updated_time_before: Union[Unset, str] = UNSET
    if not isinstance(updated_time_before, Unset):
        json_updated_time_before = updated_time_before.isoformat()
    params["updated_time_before"] = json_updated_time_before

    json_uploaded_time_after: Union[Unset, str] = UNSET
    if not isinstance(uploaded_time_after, Unset):
        json_uploaded_time_after = uploaded_time_after.isoformat()
    params["uploaded_time_after"] = json_uploaded_time_after

    json_uploaded_time_before: Union[Unset, str] = UNSET
    if not isinstance(uploaded_time_before, Unset):
        json_uploaded_time_before = uploaded_time_before.isoformat()
    params["uploaded_time_before"] = json_uploaded_time_before

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/videos/",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[PaginatedVideoList]:
    if response.status_code == 200:
        response_200 = PaginatedVideoList.from_dict(response.json())

        return response_200
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[PaginatedVideoList]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    categories_name_icontains: Union[Unset, list[str]] = UNSET,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    creator_email: Union[Unset, str] = UNSET,
    duration: Union[Unset, str] = UNSET,
    duration_gt: Union[Unset, str] = UNSET,
    duration_gte: Union[Unset, str] = UNSET,
    duration_lt: Union[Unset, str] = UNSET,
    duration_lte: Union[Unset, str] = UNSET,
    framerate: Union[Unset, int] = UNSET,
    has_tono_records: Union[Unset, bool] = UNSET,
    is_filler: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    organization: Union[Unset, int] = UNSET,
    played_count_web: Union[Unset, int] = UNSET,
    played_count_web_gt: Union[Unset, int] = UNSET,
    played_count_web_gte: Union[Unset, int] = UNSET,
    played_count_web_lt: Union[Unset, int] = UNSET,
    played_count_web_lte: Union[Unset, int] = UNSET,
    publish_on_web: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    ref_url: Union[Unset, str] = UNSET,
    ref_url_icontains: Union[Unset, str] = UNSET,
    ref_url_startswith: Union[Unset, str] = UNSET,
    updated_time_after: Union[Unset, datetime.datetime] = UNSET,
    updated_time_before: Union[Unset, datetime.datetime] = UNSET,
    uploaded_time_after: Union[Unset, datetime.datetime] = UNSET,
    uploaded_time_before: Union[Unset, datetime.datetime] = UNSET,
) -> Response[PaginatedVideoList]:
    """List of videos

    Query parameters
    ----------------

    `q` - Free search query.

    `page_size` - How many items per page. If set to 0 it will list
                  all items.  Default is 50 items.

    `ordering` - Order results by specified field.  Prepend a minus for
                 descending order.  I.e. `?ordering=-id`.

    `creator__email` - the email of the video's creator

    `framerate` - the framerate in hz * 1000

    `has_tono_records` - if the tono flag is set (true/false)

    `is_filler` - if this is a filler video (true/false)

    `name` - the exact name/title of the video

    `name__icontains` - substring is part of name/title of the video

    `organization` - Frikanalen ID of organization behind video

    `played_count_web` - the number of times this video was played on the web

    `played_count_web__gt` - greater than

    `played_count_web__gte` - greater than or equal

    `played_count_web__lt`  - less than

    `played_count_web__lte` - less than or equal

    `publish_on_web` - if this video is published ont the web (true/false)

    `proper_import` - if the uploaded video was properly imported (true/false)

    `ref_url` - the exact reference url

    `ref_url__startswith` - the reference url start with this string

    `ref_url__icontains` - the reference url contain this string

    Args:
        categories_name_icontains (Union[Unset, list[str]]):
        created_time_after (Union[Unset, datetime.datetime]):
        created_time_before (Union[Unset, datetime.datetime]):
        creator_email (Union[Unset, str]):
        duration (Union[Unset, str]):
        duration_gt (Union[Unset, str]):
        duration_gte (Union[Unset, str]):
        duration_lt (Union[Unset, str]):
        duration_lte (Union[Unset, str]):
        framerate (Union[Unset, int]):
        has_tono_records (Union[Unset, bool]):
        is_filler (Union[Unset, bool]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        organization (Union[Unset, int]):
        played_count_web (Union[Unset, int]):
        played_count_web_gt (Union[Unset, int]):
        played_count_web_gte (Union[Unset, int]):
        played_count_web_lt (Union[Unset, int]):
        played_count_web_lte (Union[Unset, int]):
        publish_on_web (Union[Unset, bool]):
        q (Union[Unset, str]):
        ref_url (Union[Unset, str]):
        ref_url_icontains (Union[Unset, str]):
        ref_url_startswith (Union[Unset, str]):
        updated_time_after (Union[Unset, datetime.datetime]):
        updated_time_before (Union[Unset, datetime.datetime]):
        uploaded_time_after (Union[Unset, datetime.datetime]):
        uploaded_time_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVideoList]
    """

    kwargs = _get_kwargs(
        categories_name_icontains=categories_name_icontains,
        created_time_after=created_time_after,
        created_time_before=created_time_before,
        creator_email=creator_email,
        duration=duration,
        duration_gt=duration_gt,
        duration_gte=duration_gte,
        duration_lt=duration_lt,
        duration_lte=duration_lte,
        framerate=framerate,
        has_tono_records=has_tono_records,
        is_filler=is_filler,
        limit=limit,
        name=name,
        name_icontains=name_icontains,
        offset=offset,
        ordering=ordering,
        organization=organization,
        played_count_web=played_count_web,
        played_count_web_gt=played_count_web_gt,
        played_count_web_gte=played_count_web_gte,
        played_count_web_lt=played_count_web_lt,
        played_count_web_lte=played_count_web_lte,
        publish_on_web=publish_on_web,
        q=q,
        ref_url=ref_url,
        ref_url_icontains=ref_url_icontains,
        ref_url_startswith=ref_url_startswith,
        updated_time_after=updated_time_after,
        updated_time_before=updated_time_before,
        uploaded_time_after=uploaded_time_after,
        uploaded_time_before=uploaded_time_before,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    categories_name_icontains: Union[Unset, list[str]] = UNSET,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    creator_email: Union[Unset, str] = UNSET,
    duration: Union[Unset, str] = UNSET,
    duration_gt: Union[Unset, str] = UNSET,
    duration_gte: Union[Unset, str] = UNSET,
    duration_lt: Union[Unset, str] = UNSET,
    duration_lte: Union[Unset, str] = UNSET,
    framerate: Union[Unset, int] = UNSET,
    has_tono_records: Union[Unset, bool] = UNSET,
    is_filler: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    organization: Union[Unset, int] = UNSET,
    played_count_web: Union[Unset, int] = UNSET,
    played_count_web_gt: Union[Unset, int] = UNSET,
    played_count_web_gte: Union[Unset, int] = UNSET,
    played_count_web_lt: Union[Unset, int] = UNSET,
    played_count_web_lte: Union[Unset, int] = UNSET,
    publish_on_web: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    ref_url: Union[Unset, str] = UNSET,
    ref_url_icontains: Union[Unset, str] = UNSET,
    ref_url_startswith: Union[Unset, str] = UNSET,
    updated_time_after: Union[Unset, datetime.datetime] = UNSET,
    updated_time_before: Union[Unset, datetime.datetime] = UNSET,
    uploaded_time_after: Union[Unset, datetime.datetime] = UNSET,
    uploaded_time_before: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[PaginatedVideoList]:
    """List of videos

    Query parameters
    ----------------

    `q` - Free search query.

    `page_size` - How many items per page. If set to 0 it will list
                  all items.  Default is 50 items.

    `ordering` - Order results by specified field.  Prepend a minus for
                 descending order.  I.e. `?ordering=-id`.

    `creator__email` - the email of the video's creator

    `framerate` - the framerate in hz * 1000

    `has_tono_records` - if the tono flag is set (true/false)

    `is_filler` - if this is a filler video (true/false)

    `name` - the exact name/title of the video

    `name__icontains` - substring is part of name/title of the video

    `organization` - Frikanalen ID of organization behind video

    `played_count_web` - the number of times this video was played on the web

    `played_count_web__gt` - greater than

    `played_count_web__gte` - greater than or equal

    `played_count_web__lt`  - less than

    `played_count_web__lte` - less than or equal

    `publish_on_web` - if this video is published ont the web (true/false)

    `proper_import` - if the uploaded video was properly imported (true/false)

    `ref_url` - the exact reference url

    `ref_url__startswith` - the reference url start with this string

    `ref_url__icontains` - the reference url contain this string

    Args:
        categories_name_icontains (Union[Unset, list[str]]):
        created_time_after (Union[Unset, datetime.datetime]):
        created_time_before (Union[Unset, datetime.datetime]):
        creator_email (Union[Unset, str]):
        duration (Union[Unset, str]):
        duration_gt (Union[Unset, str]):
        duration_gte (Union[Unset, str]):
        duration_lt (Union[Unset, str]):
        duration_lte (Union[Unset, str]):
        framerate (Union[Unset, int]):
        has_tono_records (Union[Unset, bool]):
        is_filler (Union[Unset, bool]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        organization (Union[Unset, int]):
        played_count_web (Union[Unset, int]):
        played_count_web_gt (Union[Unset, int]):
        played_count_web_gte (Union[Unset, int]):
        played_count_web_lt (Union[Unset, int]):
        played_count_web_lte (Union[Unset, int]):
        publish_on_web (Union[Unset, bool]):
        q (Union[Unset, str]):
        ref_url (Union[Unset, str]):
        ref_url_icontains (Union[Unset, str]):
        ref_url_startswith (Union[Unset, str]):
        updated_time_after (Union[Unset, datetime.datetime]):
        updated_time_before (Union[Unset, datetime.datetime]):
        uploaded_time_after (Union[Unset, datetime.datetime]):
        uploaded_time_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVideoList
    """

    return sync_detailed(
        client=client,
        categories_name_icontains=categories_name_icontains,
        created_time_after=created_time_after,
        created_time_before=created_time_before,
        creator_email=creator_email,
        duration=duration,
        duration_gt=duration_gt,
        duration_gte=duration_gte,
        duration_lt=duration_lt,
        duration_lte=duration_lte,
        framerate=framerate,
        has_tono_records=has_tono_records,
        is_filler=is_filler,
        limit=limit,
        name=name,
        name_icontains=name_icontains,
        offset=offset,
        ordering=ordering,
        organization=organization,
        played_count_web=played_count_web,
        played_count_web_gt=played_count_web_gt,
        played_count_web_gte=played_count_web_gte,
        played_count_web_lt=played_count_web_lt,
        played_count_web_lte=played_count_web_lte,
        publish_on_web=publish_on_web,
        q=q,
        ref_url=ref_url,
        ref_url_icontains=ref_url_icontains,
        ref_url_startswith=ref_url_startswith,
        updated_time_after=updated_time_after,
        updated_time_before=updated_time_before,
        uploaded_time_after=uploaded_time_after,
        uploaded_time_before=uploaded_time_before,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    categories_name_icontains: Union[Unset, list[str]] = UNSET,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    creator_email: Union[Unset, str] = UNSET,
    duration: Union[Unset, str] = UNSET,
    duration_gt: Union[Unset, str] = UNSET,
    duration_gte: Union[Unset, str] = UNSET,
    duration_lt: Union[Unset, str] = UNSET,
    duration_lte: Union[Unset, str] = UNSET,
    framerate: Union[Unset, int] = UNSET,
    has_tono_records: Union[Unset, bool] = UNSET,
    is_filler: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    organization: Union[Unset, int] = UNSET,
    played_count_web: Union[Unset, int] = UNSET,
    played_count_web_gt: Union[Unset, int] = UNSET,
    played_count_web_gte: Union[Unset, int] = UNSET,
    played_count_web_lt: Union[Unset, int] = UNSET,
    played_count_web_lte: Union[Unset, int] = UNSET,
    publish_on_web: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    ref_url: Union[Unset, str] = UNSET,
    ref_url_icontains: Union[Unset, str] = UNSET,
    ref_url_startswith: Union[Unset, str] = UNSET,
    updated_time_after: Union[Unset, datetime.datetime] = UNSET,
    updated_time_before: Union[Unset, datetime.datetime] = UNSET,
    uploaded_time_after: Union[Unset, datetime.datetime] = UNSET,
    uploaded_time_before: Union[Unset, datetime.datetime] = UNSET,
) -> Response[PaginatedVideoList]:
    """List of videos

    Query parameters
    ----------------

    `q` - Free search query.

    `page_size` - How many items per page. If set to 0 it will list
                  all items.  Default is 50 items.

    `ordering` - Order results by specified field.  Prepend a minus for
                 descending order.  I.e. `?ordering=-id`.

    `creator__email` - the email of the video's creator

    `framerate` - the framerate in hz * 1000

    `has_tono_records` - if the tono flag is set (true/false)

    `is_filler` - if this is a filler video (true/false)

    `name` - the exact name/title of the video

    `name__icontains` - substring is part of name/title of the video

    `organization` - Frikanalen ID of organization behind video

    `played_count_web` - the number of times this video was played on the web

    `played_count_web__gt` - greater than

    `played_count_web__gte` - greater than or equal

    `played_count_web__lt`  - less than

    `played_count_web__lte` - less than or equal

    `publish_on_web` - if this video is published ont the web (true/false)

    `proper_import` - if the uploaded video was properly imported (true/false)

    `ref_url` - the exact reference url

    `ref_url__startswith` - the reference url start with this string

    `ref_url__icontains` - the reference url contain this string

    Args:
        categories_name_icontains (Union[Unset, list[str]]):
        created_time_after (Union[Unset, datetime.datetime]):
        created_time_before (Union[Unset, datetime.datetime]):
        creator_email (Union[Unset, str]):
        duration (Union[Unset, str]):
        duration_gt (Union[Unset, str]):
        duration_gte (Union[Unset, str]):
        duration_lt (Union[Unset, str]):
        duration_lte (Union[Unset, str]):
        framerate (Union[Unset, int]):
        has_tono_records (Union[Unset, bool]):
        is_filler (Union[Unset, bool]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        organization (Union[Unset, int]):
        played_count_web (Union[Unset, int]):
        played_count_web_gt (Union[Unset, int]):
        played_count_web_gte (Union[Unset, int]):
        played_count_web_lt (Union[Unset, int]):
        played_count_web_lte (Union[Unset, int]):
        publish_on_web (Union[Unset, bool]):
        q (Union[Unset, str]):
        ref_url (Union[Unset, str]):
        ref_url_icontains (Union[Unset, str]):
        ref_url_startswith (Union[Unset, str]):
        updated_time_after (Union[Unset, datetime.datetime]):
        updated_time_before (Union[Unset, datetime.datetime]):
        uploaded_time_after (Union[Unset, datetime.datetime]):
        uploaded_time_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[PaginatedVideoList]
    """

    kwargs = _get_kwargs(
        categories_name_icontains=categories_name_icontains,
        created_time_after=created_time_after,
        created_time_before=created_time_before,
        creator_email=creator_email,
        duration=duration,
        duration_gt=duration_gt,
        duration_gte=duration_gte,
        duration_lt=duration_lt,
        duration_lte=duration_lte,
        framerate=framerate,
        has_tono_records=has_tono_records,
        is_filler=is_filler,
        limit=limit,
        name=name,
        name_icontains=name_icontains,
        offset=offset,
        ordering=ordering,
        organization=organization,
        played_count_web=played_count_web,
        played_count_web_gt=played_count_web_gt,
        played_count_web_gte=played_count_web_gte,
        played_count_web_lt=played_count_web_lt,
        played_count_web_lte=played_count_web_lte,
        publish_on_web=publish_on_web,
        q=q,
        ref_url=ref_url,
        ref_url_icontains=ref_url_icontains,
        ref_url_startswith=ref_url_startswith,
        updated_time_after=updated_time_after,
        updated_time_before=updated_time_before,
        uploaded_time_after=uploaded_time_after,
        uploaded_time_before=uploaded_time_before,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    categories_name_icontains: Union[Unset, list[str]] = UNSET,
    created_time_after: Union[Unset, datetime.datetime] = UNSET,
    created_time_before: Union[Unset, datetime.datetime] = UNSET,
    creator_email: Union[Unset, str] = UNSET,
    duration: Union[Unset, str] = UNSET,
    duration_gt: Union[Unset, str] = UNSET,
    duration_gte: Union[Unset, str] = UNSET,
    duration_lt: Union[Unset, str] = UNSET,
    duration_lte: Union[Unset, str] = UNSET,
    framerate: Union[Unset, int] = UNSET,
    has_tono_records: Union[Unset, bool] = UNSET,
    is_filler: Union[Unset, bool] = UNSET,
    limit: Union[Unset, int] = UNSET,
    name: Union[Unset, str] = UNSET,
    name_icontains: Union[Unset, str] = UNSET,
    offset: Union[Unset, int] = UNSET,
    ordering: Union[Unset, str] = UNSET,
    organization: Union[Unset, int] = UNSET,
    played_count_web: Union[Unset, int] = UNSET,
    played_count_web_gt: Union[Unset, int] = UNSET,
    played_count_web_gte: Union[Unset, int] = UNSET,
    played_count_web_lt: Union[Unset, int] = UNSET,
    played_count_web_lte: Union[Unset, int] = UNSET,
    publish_on_web: Union[Unset, bool] = UNSET,
    q: Union[Unset, str] = UNSET,
    ref_url: Union[Unset, str] = UNSET,
    ref_url_icontains: Union[Unset, str] = UNSET,
    ref_url_startswith: Union[Unset, str] = UNSET,
    updated_time_after: Union[Unset, datetime.datetime] = UNSET,
    updated_time_before: Union[Unset, datetime.datetime] = UNSET,
    uploaded_time_after: Union[Unset, datetime.datetime] = UNSET,
    uploaded_time_before: Union[Unset, datetime.datetime] = UNSET,
) -> Optional[PaginatedVideoList]:
    """List of videos

    Query parameters
    ----------------

    `q` - Free search query.

    `page_size` - How many items per page. If set to 0 it will list
                  all items.  Default is 50 items.

    `ordering` - Order results by specified field.  Prepend a minus for
                 descending order.  I.e. `?ordering=-id`.

    `creator__email` - the email of the video's creator

    `framerate` - the framerate in hz * 1000

    `has_tono_records` - if the tono flag is set (true/false)

    `is_filler` - if this is a filler video (true/false)

    `name` - the exact name/title of the video

    `name__icontains` - substring is part of name/title of the video

    `organization` - Frikanalen ID of organization behind video

    `played_count_web` - the number of times this video was played on the web

    `played_count_web__gt` - greater than

    `played_count_web__gte` - greater than or equal

    `played_count_web__lt`  - less than

    `played_count_web__lte` - less than or equal

    `publish_on_web` - if this video is published ont the web (true/false)

    `proper_import` - if the uploaded video was properly imported (true/false)

    `ref_url` - the exact reference url

    `ref_url__startswith` - the reference url start with this string

    `ref_url__icontains` - the reference url contain this string

    Args:
        categories_name_icontains (Union[Unset, list[str]]):
        created_time_after (Union[Unset, datetime.datetime]):
        created_time_before (Union[Unset, datetime.datetime]):
        creator_email (Union[Unset, str]):
        duration (Union[Unset, str]):
        duration_gt (Union[Unset, str]):
        duration_gte (Union[Unset, str]):
        duration_lt (Union[Unset, str]):
        duration_lte (Union[Unset, str]):
        framerate (Union[Unset, int]):
        has_tono_records (Union[Unset, bool]):
        is_filler (Union[Unset, bool]):
        limit (Union[Unset, int]):
        name (Union[Unset, str]):
        name_icontains (Union[Unset, str]):
        offset (Union[Unset, int]):
        ordering (Union[Unset, str]):
        organization (Union[Unset, int]):
        played_count_web (Union[Unset, int]):
        played_count_web_gt (Union[Unset, int]):
        played_count_web_gte (Union[Unset, int]):
        played_count_web_lt (Union[Unset, int]):
        played_count_web_lte (Union[Unset, int]):
        publish_on_web (Union[Unset, bool]):
        q (Union[Unset, str]):
        ref_url (Union[Unset, str]):
        ref_url_icontains (Union[Unset, str]):
        ref_url_startswith (Union[Unset, str]):
        updated_time_after (Union[Unset, datetime.datetime]):
        updated_time_before (Union[Unset, datetime.datetime]):
        uploaded_time_after (Union[Unset, datetime.datetime]):
        uploaded_time_before (Union[Unset, datetime.datetime]):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        PaginatedVideoList
    """

    return (
        await asyncio_detailed(
            client=client,
            categories_name_icontains=categories_name_icontains,
            created_time_after=created_time_after,
            created_time_before=created_time_before,
            creator_email=creator_email,
            duration=duration,
            duration_gt=duration_gt,
            duration_gte=duration_gte,
            duration_lt=duration_lt,
            duration_lte=duration_lte,
            framerate=framerate,
            has_tono_records=has_tono_records,
            is_filler=is_filler,
            limit=limit,
            name=name,
            name_icontains=name_icontains,
            offset=offset,
            ordering=ordering,
            organization=organization,
            played_count_web=played_count_web,
            played_count_web_gt=played_count_web_gt,
            played_count_web_gte=played_count_web_gte,
            played_count_web_lt=played_count_web_lt,
            played_count_web_lte=played_count_web_lte,
            publish_on_web=publish_on_web,
            q=q,
            ref_url=ref_url,
            ref_url_icontains=ref_url_icontains,
            ref_url_startswith=ref_url_startswith,
            updated_time_after=updated_time_after,
            updated_time_before=updated_time_before,
            uploaded_time_after=uploaded_time_after,
            uploaded_time_before=uploaded_time_before,
        )
    ).parsed
