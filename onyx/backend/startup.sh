#!/bin/sh

gunicorn -b "${HOST:?}":"${PORT:?}" onyx.app:app